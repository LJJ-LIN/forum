from django.shortcuts import render,redirect
from article.models import Article
from block.models import Block
from article.forms import ArticleForm
from django.views.generic import View,DetailView
from django.core.paginator import Paginator

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
			article.block = self.block
			article.status = 0
			article.save()
			form.save_m2m()
			return redirect("/article/list/%s"  %self.block_id)
		else:
			return render(request,self.template_name,{"b":self.block,"form":form})

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article_detail.html'
	context_object_name='a'
		
		

def article_list(request, block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
	p = Paginator(all_articles,1)
	page_no = request.GET.get('page_no')
	page = p.page(page_no)
	article_objs = page.object_list
	return render(request,"article_list.html",{"articles":page,"b":block,"all":article_objs})



	
	

