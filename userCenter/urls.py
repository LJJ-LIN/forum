from django.conf.urls import url
from userCenter.view import upload_avatar

urlpatterns = [
         url(r'^uploadavatar/', upload_avatar),
]