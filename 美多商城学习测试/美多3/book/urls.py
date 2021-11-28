from django.urls import path
from django.urls import converters
from book.views import create_book,shop,register,json,method,res,respone,rdict
from django.urls import register_converter
#定义转换器
class MobileConverter:
    # 验证的关键是正则式
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

register_converter(MobileConverter,'phone')

urlpatterns=[
    path('create/',create_book),
    # #一行的路由
    # path('11000/11005/',shop),
    #占位符来 代表大量的路由索引
    # <转换器：变量名> 作用：对变量进行类型验证
    path('<int:city_id>/<phone:mobile>/',shop),
    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('res/',res),
    path('response/',respone),
    path('rdict/',rdict),
]