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
  charfield 必须设置max_length
  verbose_name 主要是站点使用
2.改变表的名称
  默认的表的名称是：子应用名_类名 且都是小写
  修改表的类名
"""
class BookInfo(models.Model):
    name=models.CharField(max_length=10,unique=True)
    pub_date=models.DateField(null=True)
    readcount=models.SmallIntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)
    #修改表的名称（固定的写法）
    class Meta:
        db_table='bookinfo'
        #admin站点使用
        verbose_name='书籍管理'