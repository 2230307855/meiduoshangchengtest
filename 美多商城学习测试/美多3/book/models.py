#每次models的文件的内容发生变化，都要执行迁移
from django.db import models

# Create your models here.
"""
模型类要继承自djaogo的models.Models
1.定义属性
  属性名不要用连续的下划线
  属性名=models.类型（选项）
    属性名 对应 就是字段名
  类型就是mysql里的类型
  选项  是否有默认值、为1、为null
  chcharfield 必须设置max_length
  verbose_name 主要是站点使用
2.改变表的名称
  默认的表的名称是：子应用名_类名 且都是小写
  修改表的类名
"""
class BookInfo(models.Model):
    name=models.CharField(max_length=20,verbose_name='名称')
    pub_date=models.DateField(null=True,verbose_name='发布日期')
    readcount=models.SmallIntegerField(default=0,verbose_name='阅读量')
    commentcount=models.IntegerField(default=0,verbose_name='评论量')
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除')

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
    #修改表的名称（固定的写法）
    class Meta:
        db_table='bookinfo'
        #admin站点使用
        verbose_name='图书'


class PeopleInfo(models.Model):
    #定义一个有序字典
    GENDER_CHOICE=((1,'male'),(2,'female'))
    name=models.CharField(max_length=20,verbose_name='名称')
    #让性别从自己定义的键值元组中选择
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,default=0,verbose_name='性别')
    description=models.CharField(max_length=100,verbose_name='描述信息')
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除')
    #系统会自动为外键添加下划线id，自己不用加
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='图书')
    #外键的级联操作
    #SET_NULL 设置为空
    #PROTECTED 抛出异常，不让删除
    #CASCADE 级联删除
    #
    def __str__(self):
        return self.name

    class Meta:
        db_table='peopleinfo'
        verbose_name='人物信息'
