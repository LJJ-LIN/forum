from django.db import models
from block.models import Block
from django.contrib.auth.models import User
import pytz

class DeletedCommentManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status=-1)

class CommentManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status=0)
		
		

class Article(models.Model):
	objects = models.Manager()   #默认的
	normal_objects = CommentManager()
	deleted_objects = DeletedCommentManager()
	BEIJING_TZ = pytz.timezone('Asia/Shanghai')
	owner = models.ForeignKey(User,verbose_name="作者")
	block = models.ForeignKey(Block,verbose_name="板块ID")
	title = models.CharField("名称",max_length=100)
	content = models.CharField("描述",max_length=10000)
	status = models.IntegerField("状态",choices=((0,"正常"),(-1,"删除")))
	create_timestamp = models.DateTimeField("创建时间",auto_now_add=True)
	last_update_timestamp = models.DateTimeField("最后更新事件",auto_now=True)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name="文章"
		verbose_name_plural = "文章"

class  Comment(models.Model):
	objects = models.Manager()   #默认的
	normal_objects = CommentManager()
	deleted_objects = DeletedCommentManager()
	BEIJING_TZ = pytz.timezone('Asia/Shanghai')
	owner = models.ForeignKey(User,verbose_name="作者")
	article = models.ForeignKey(Article,verbose_name="文章ID")
	content = models.CharField("评论",max_length=10000)
	status = models.IntegerField("状态",choices=((0,"正常"),(-1,"删除")))
	create_timestamp = models.DateTimeField("创建时间",auto_now_add=True)
	last_update_timestamp = models.DateTimeField("最后更新事件",auto_now=True)

	def __str__(self):
		return self.content

	class Meta:
		verbose_name="评论"
		verbose_name_plural = "评论"			
			

		