"""美多 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from book.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # #1.查询导入法(子应用不添加urls文件)（路由 ，视图函数名）
    # path('index/',index),
    # 2.导入include头，并在子应用中创建urls文件
    path('',include('book.urls'))
]
