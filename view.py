from django.http import HttpResponse
from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User
from activate.models import ActivateCode 
import uuid
import datetime
from django.core.mail import send_mail
from django.utils import timezone

def index(request):
	block_infos = Block.normal_objects.order_by("-id")
	return render(request,"index.html",{"blocks":block_infos})

def  register(request):
	error = ""
	if request.method == "GET":
		return render(request,'register.html')
	else:
		owner = request.POST['username'].strip()
		email = request.POST['email'].strip()
		password = request.POST['password'].strip()
		password_check = request.POST['password_check'].strip()

		if not owner or not password or not email:
			error = "任何字段都不能为空"
		if password != password_check:
			error = "两次密码不一致"
		if User.objects.filter(username=owner).count() >0:
			error = "用户名已存在"
		if not error:
			user = User.objects.create_user(username = owner,email =email,password = password)
			user.save()

			new_code = str(uuid.uuid4()).replace('-','')
			expire_time = timezone.now()+datetime.timedelta(days=2)
			code_recode = ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
			code_recode.save()

			activate_link = "http://%s/activate/%s" %(request.get_host(),new_code)
			activate_email = '''点击<a href="%s">这里</a>激活''' % activate_link
			send_mail(subject='[python部落论坛]激活邮件',
			message='点击链接激活:%s' %activate_link,
			from_email='672731931@qq.com',
			recipient_list=[email],
			fail_silently=False)
		else:
			return render(request,"register.html",{"error":error})
		return render(request,'success_hint.html',{'msg':'注册成功，请前往你的邮箱完成验证!'})

def notfound(request):
	return render(request,"404.html")