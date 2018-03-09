from django.shortcuts import render
from django.http import HttpResponse


#from models import Test 为什么不行？？？

from . import models

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