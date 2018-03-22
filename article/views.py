from django.shortcuts import render,redirect
from article.models import Article,Comment
from block.models import Block
from article.forms import ArticleForm,CommentForm
from django.views.generic import View,DetailView
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

#创建文章
class ArticleCreateView(View):

	template_name = "article_create.html"

	def init_data(self,block_id):
		self.block_id = block_id
		self.block = Block.objects.get(id=block_id)

	def get(self,request,block_id):
		self.init_data(block_id)
		return render(request,self.template_name,{'b':self.block})

	def  post(self,request,block_id):
		self.init_data(block_id)
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.owner = request.user
			article.block = self.block
			article.status = 0
			article.save()
			form.save_m2m()
			return redirect("/article/list/%s?page_no=1"  %self.block_id)
		else:
			return render(request,self.template_name,{"b":self.block,"form":form})
#文章详情页	
class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article_detail.html'
	context_object_name='article'
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		page_no = int(self.request.GET.get("page_no",1))
		all_comments = Comment.objects.filter(article=context["article"],status=0)
		comments, pagination_data = paginate_queryset(all_comments, page_no, cnt_per_page=3)
		context['comments'] = comments
		context['pagination_data']=pagination_data
		return context

#文章详情页中发表评论
def create_comment(request):
	article_id = int(request.POST['article_id'])
	article = Article.normal_objects.get(id = article_id)
	form = CommentForm(request.POST)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.owner = request.user
		comment.article = article
		comment.status = 0
		comment.save()
		status = "ok"
		msg = ""
	else:
		status = "err"
		msg = "错误信息"
	return json_response({"status":status,"msg":msg})

def json_response(obj):
	txt = json.dumps(obj)
	return HttpResponse(txt)

#文章列表
def article_list(request, block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	all_articles = Article.normal_objects.filter(block=block).order_by("-id")
	p = Paginator(all_articles,3)
	page_no = int(request.GET.get("page_no","1"))

	page_articles, pagination_data = paginate_queryset(all_articles,page_no)
	return render(request,"article_list.html",{"articles":page_articles,"b":block,
		           "pagination_data":pagination_data})

#处理分页列表
def paginate_queryset(objs, page_no, cnt_per_page=3, half_show_length=5):
	p = Paginator(objs, cnt_per_page)
	if page_no > p.num_pages:
		page_no = p.num_pages
	if page_no <= 0:
		page_no = 1
	page_links = [i for i in range(page_no - half_show_length, page_no+half_show_length+1)
	                     if i >0 and i <= p.num_pages]
	page = p.page(page_no)
	previous_link = page_links[0] - 1
	next_link = page_links[-1] + 1
	pagination_data = {"has_previous":previous_link > 0,
	                            "has_next":next_link <= p.num_pages,
	                            "previous_link":previous_link,
	                            "next_link":next_link,
	                            "page_cnt":p.num_pages,
	                            "current_no":page_no,
	                            "page_links":page_links}
	return (page.object_list, pagination_data)


	
	

