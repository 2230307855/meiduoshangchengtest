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
##################################
#F对象
from django.db.models import F
#两个属性的比较
#格式 以filter为例
# 模型类名.objects.filter(属性名__运算符=F('第二个属性名'))
#！！！！！！！！！！
#查询阅读量大于评论量的书籍
BookInfo.objects.filter(readcount__gte=F('commentcount'))
#查询阅读量大于两倍评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
##################################
#Q对象
#并且查询
#查询阅读量大于20，并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

#或者查询
from django.db.models import Q
#语法
#模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|....)
#用Q实现并且
#模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&Q....)
#Q非
#模型类名.objects.filter(~Q(属性名__运算符=值)&Q(属性名__运算符=值)&Q....)
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
########################################################
#聚合函数：Sum、Max、Min、Avg、Count
from django.db.models import Sum,Max,Min,Avg,Count

#样例 模型类名.objects.aggregate(Xxx('字段名'))
BookInfo.objects.aggregate(Sum('readcount'))
#########################################################
#排序
BookInfo.objects.all().order_by('readcount')#升序
BookInfo.objects.all().order_by('-readcount')#降序
####################################################
#级联查询
#查询书籍为1的所有人物信息
book=BookInfo.objects.get(id=1)#一对多查询
#一到多的访问/利用系统添加的访问关联模型类_set来实现
book.peopleinfo_set.all()
PeopleInfo.objects.filter(book=1)
#查询人物为1的书籍信息
person=PeopleInfo.objects.get(id=1)
person.book
person.book.name
####################################################
#关联查询的过滤查询
#模型类名.objects.(关联模型名小写__字段名__运算符=值)
#查询图书 要求图书人物为 郭靖
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')
#查询图书 要求图书中人物描述包含“八”
BookInfo.objects.filter(peopleinfo__description__contains='八')
#查询书名是‘天龙八部’的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__name__iexact='天龙八部')
#查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__commentcount__gt=30)