from django.shortcuts import render

# Create your views here.
# def index(request):
##############################################################
#增加数据
from book.models import BookInfo
#方式1  必须要电泳对象的即book的save()方法
book=BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
book.save()
#方式2
#objects
#相当于对象的一个代理，帮我们实现增删改查
# 卧槽真的舒服
BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-1-1',
    readcount=100
)
##############################################################
#修改数据
#1.
#涉及到查询 而且要调用save()方法
#select * from bookinfo where id=6
book=BookInfo.objects.get(id=6)
book.name='运维开发入门'
book.save()
#方法2
#查询与更新同步 牛批
BookInfo.objects.filter(id=6).update(
    name='爬虫入门',
    commentcount=666
)
##############################################################
#修改数据
#1.
#删除数据
book=BookInfo.objects.get(id=6)
#物理删除 逻辑删除
book.delete()
#2.查询删除
# BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=6).delete()