from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from myapp.models import Article


def index(request):
     # 这里处理模型
     article_list = Article.objects.order_by('title')
     context = {
        "blog_list": article_list
     }
     return render(request, 'blog.html', context)