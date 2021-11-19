from django.urls import path
from book.views import create_book,shop
urlpatterns={
    path('create/',create_book),
    # #一行的路由
    # path('11000/11005/',shop),
    #占位符来 代表大量的路由索引
    path('<city_id>/<shop_id>/',shop),
}