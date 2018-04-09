from django.conf.urls import url
from article.views import article_list,ArticleCreateView,ArticleDetailView,create_comment
from django.contrib.auth.decorators import login_required

urlpatterns = [
      url(r'^list/(?P<block_id>\d+)',article_list),
      url(r'^create/(?P<block_id>\d+)',login_required(ArticleCreateView.as_view())),
      url(r'^articledetail/(?P<pk>\d+)$', ArticleDetailView.as_view()),
      url(r'^articledetail/comment/create/', create_comment),
      
]