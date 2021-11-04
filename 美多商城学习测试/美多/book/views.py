from django.shortcuts import render

# Create your views here.

#视图函数有两个要求
#请求 第一个参数
#相应 第二个参数
from django.http import HttpResponse

def index(request):
    return HttpResponse("ok")