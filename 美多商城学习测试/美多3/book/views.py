from django.http import HttpResponse
from django.shortcuts import render, redirect
from book.models import BookInfo
# Create your views here.
def create_book(request):
    book=BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )
    return HttpResponse('create')

def shop(request,city_id,mobile):
    import re
    # print('city_id is:',city_id,' shop_id is:',shop_id)
    # 验证方案一
    # if not re.match('\d{5}',shop_id):
    #     return HttpResponse('无此商品')
    #验证方案二

    query_params=request.GET
    print(query_params)
    # order=query_params.get('order')
    # order=query_params['order']#如果多个值，选择最后赋予的值
    #如果要的到所有的值，要用 order=query_params.getlist('order')
    # print(order)
    return HttpResponse('我的饭店')
#<QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']}>
#QueryDict 具有字典的特性
#可以一键多指


###############################################
"""
查询字符串
http://ip:port/path/path/?key=value&key1=value1
url 以 ？ 来进行分割  分为2部分
？前边为 请求路径
？后边为 查询的字符串  类似于字典key=value 多个用&连接

"""

def register(request):
    data=request.POST
    print(data)
    return HttpResponse("ok")

def json(request):
    import json
    body=request.body
    body_str=body.decode()
    # 解码成str类型
    """
    {
    "name": "itcast",
    "age":10
    }
    """
    # 转为python的字典
    body_dict=json.loads(body_str)
    print(body_dict)
    print(request.META['SERVER_PORT'])
    return HttpResponse("json")

def method(request):
    print(request.method)
    return HttpResponse('method')

def res(request):
    response =HttpResponse('res',status=200)
    response['name']='itcast'
    return response
#相应状态只能从1-599
#4xx 请求有问题 404路由问题 403禁止访问 权限问题
#200 成功
#1xx 消息
#3xx 重定向
#5xx 服务器错误
from django.http import HttpResponse,JsonResponse
def respone(request):
    info={
        'name':'itcast',
        'sddress':'shunyi'
    }
    girl_friends=[
        {
            'name': 'itcast',
            'sddress': 'shunyi'
        },
        {
            'name': 'itcast',
            'sddress': 'shunyi'
        }
    ]

    respone=JsonResponse(data=girl_friends,safe=False)
    #sfe=true表示数据必须是字典
    #如果给一个非字典数据，safe=false
    return respone

def rdict(request):
    return redirect('https://www.baidu.com/default.html')