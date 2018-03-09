from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	#why does it require request param?
    return render(request,'index.html',{"name":"saltfish","learnning":{"python":1,"js":2}})