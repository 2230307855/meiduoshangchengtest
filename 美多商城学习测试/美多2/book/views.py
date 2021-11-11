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
####################################################
#查询
#get （单一对象）（精确查询）
# try:
#     book=BookInfo.objects.get(id=1)
# except BookInfo.DoesNotExist:
#     print('查询的结果不存在')
# #
#all
# books=BookInfo.objects.all()
#获取所有的人数
from book.models import PeopleInfo
# peoples=PeopleInfo.objects.all()
renshu=PeopleInfo.objects.all().count()
#filter(过滤查询)
#联合使用的函数：
# filter过滤出多个结果 exclude排除掉符合条件
# get过滤获取单一的结果

#模型类名.objects.filter(属性名__运算符=值) n个结果
#模型类名.objects.exclude(属性名__运算符=值) n个结果
#模型类名.objects.get(属性名__运算符=值)  1个结果或者异常

#查询编号为1的图书
book=BookInfo.objects.get(id=1)
BookInfo.objects.get(pk=1)#主键获取对象
#查询书名中包含湖的书
BookInfo.objects.filter(name__contains='湖')
#查询书名以部结尾的图书
BookInfo.objects.filter(name__endswith='部')
#查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
#查询编号为1|2|5的图书
BookInfo.objects.filter(id__in=[1,3,5])
#查询编号大于3的书
#gt lt gte lte
BookInfo.objects.filter(id__gt=3)
#查询编号不等于3的书籍 exclude 排除id=3的书
BookInfo.objects.exclude(id=3)
#查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
#查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')