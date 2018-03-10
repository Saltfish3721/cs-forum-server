from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):

    articleInfos = models.articleInfo.objects.all()[:7]
    print(articleInfos)#<QuerySet [<articleInfo: first!!!>, <articleInfo: secont!!!!>]>
    print(articleInfos[0])#first!!!
    print(type(articleInfos[0]))#<class 'boards.models.articleInfo'>
    print(articleInfos[0].title)#first!!!
    print(articleInfos[0].info)#66666666666666
    return render(request,'index.html',{'articleInfos':articleInfos})


def article(request,articleID):

    # articleBody = models.articleBody.objects.filter(articleID=articleID)
    # print(type(articleBody))
    articleBody = models.articleBody.objects.get(pk=articleID)

    return render(request,'article.html',{'articleBody':articleBody})


def users(request):

    user = models.articleInfo.objects.get(pk=10)
    return render(request,'user.html',{'user':user})


def editarticle(request):
    return render(request,'editarticle.html')

def postarticle(request):

    title     = request.POST.get('title','TITLE')
    content   = request.POST.get('content','CONTENT')
    article = models.articleBody.objects.create(title=title,content=content)

    # authorID    = request.POST.get('authorID','authorID')
    authorID = 1
    print(type(models.articleInfo.objects.latest('articleID').articleID_id))
    articleID = models.articleInfo.objects.latest('articleID').id + 1
    models.articleInfo.objects.create(articleID=article,title=title,info=content)


    return render(request,'index.html')














# Create your views here.
def home(request):

    #confuse me...it is object or list? 动态语言就是这点不好
    # a1 =  models.Test(title="shuai",content="so x=cooooooooool!!")
    # a1.save()

    #article = models.Test.objects.all()[:5]

    #print(type(article))
    #<class 'django.db.models.query.QuerySet'>
    #因为是set类型，我该怎么把它当做一般对象使用呢？？？
    #print(len(article))

    article = models.Test.objects.get(pk=1)
    print(type(article))
    #<class 'boards.models.Test'>
    print(article)
    #Test object
    print(article.title)
    #ecpected print


	#why does it require request param?
    return render(request,'index.html',{'article':article})

    #加了一层.objects 是为了放在和自定义属性冲突吧