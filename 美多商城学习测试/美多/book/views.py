from django.shortcuts import render

# Create your views here.
"""
视图
视图函数 即python的函数
要求：
1.第一个参数接受请求
2.
"""
from django.http import HttpRequest
from django.http import HttpResponse
#我们期望用户输入 http://127.0.0.1:8000/index/
#来访问视图函数
def index(request):
    return HttpResponse("OK")
