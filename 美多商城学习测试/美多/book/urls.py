from django.urls import path
from book.views import index

urlpatterns = [
    #查询导入法（路由 ，视图函数名）
    path('index/',index),

]