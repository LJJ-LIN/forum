from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
import os

@login_required
def upload_avatar(request):
	if request.method == "GET":
		return render(request, "upload_avatar.html")
	else:
		profile = request.user.userprofile
		avatar_file = request.FILES.get("avatar", None)
		file_path = os.path.join("d:/python/workspace/forum/avatar/", avatar_file.name)
		with open(file_path, 'wb+') as destination:
			for chunk in avatar_file.chunks():
				destination.write(chunk)
		url = "http://res.myforum.com/avatar/%s"  % avatar_file.name
		profile.avatar = url
		profile.save()
		return redirect("/")