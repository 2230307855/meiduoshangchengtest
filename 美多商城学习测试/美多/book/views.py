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
    # return HttpResponse("OK")
    context={#视图的数据传递给渲染模板
        'name':'马上双十一，点我有惊喜！'
    }
    return render(request,'book/index.html',context=context)
    # 渲染函数
    # request 请求
    # template_name 模板名字
    # context 上下文
    # content_type
    # status
    # using