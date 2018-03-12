from django.conf.urls import url
from article.views import article_list

urlpatterns = [
      url(r'^list/(?P<block_id>\d+)',article_list)
]