from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):

    articles = models.article.objects.all()[:7]
   
    return render(request,'index.html',{'articles':articles})


def article(request,articleID):

    # articleBody = models.articleBody.objects.filter(title='vue!!!!'). --<QuerySet [<articleBody: vue!!!!>, <articleBody: vue!!!!>,
    article = models.article.objects.filter(articleID=articleID)#<QuerySet [<articleBody: vue!!!!>]>
    
    return render(request,'article.html',{'article':article[0]})


def users(request):

    user = models.articleInfo.objects.get(pk=10)
    return render(request,'user.html',{'user':user})


def editarticle(request):
    return render(request,'editarticle.html')

def postarticle(request):

    article         = models.article()
    article.title   = request.POST.get('title','TITLE')
    article.content = request.POST.get('content','CONTENT')
    #article = models.articleBody.objects.create(title=title,content=content)
    
    # authorID    = request.POST.get('authorID','authorID')
    
    article.save()


    return render(request,'index.html')





