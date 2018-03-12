from django.shortcuts import render
from article.models import Article
from block.models import Block

def article_list(request, block_id):
	block_id = int(block_id)
	block = Block.objects.get(id=block_id)
	article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
	return render(request,"article_list.html",{"articles":article_objs,"b":block})