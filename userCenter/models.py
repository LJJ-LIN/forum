from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.CharField("头像",max_length=300, blank=True)
	sex=models.IntegerField("性别", choices=((0,u"男"),(-1,u"女")), default=0)
	birthday=models.DateTimeField("生日", null=True, blank=True)