from django.db import models

#模型类要继承自models.Model
# Create your models here.
class BookInfo(models.Model):
    #id
    name=models.CharField(max_length=10)
    #重写方法来正确显示书籍的名字，并重新运行
    def __str__(self):
        return self.name
class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    #添加外键约束
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)