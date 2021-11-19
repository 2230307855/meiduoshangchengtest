from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.
def create_book(request):
    book=BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )
    return HttpResponse('create')

def shop(request,city_id,shop_id):
    # print('city_id is:',city_id,' shop_id is:',shop_id)
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