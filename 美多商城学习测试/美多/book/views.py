from django.shortcuts import render

# Create your views here.

#视图函数有两个要求
#请求 第一个参数
#相应 第二个参数
from django.http import HttpResponse

def index(request):
    # return HttpResponse("ok")
    context={
        'name':'马上双十一，点我有惊喜！'
    }
    return render(request,'book/index.html',context=context)
    #三个参数  请求、模板名字、context表示上下文动态数据