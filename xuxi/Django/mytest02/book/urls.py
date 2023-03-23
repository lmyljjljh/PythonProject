"""mytest02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from book.views import index, detail, set_cookie, get_cookie, set_session, get_session, LoginView, CenterView, demo, \
    HomeView, ZY

urlpatterns = [
    path("index/", index, name='index'),

    # 根据位置来获取对应id
    path("detail/<int:category_id>/<int:book_id>/", detail),

    path("set_cookie/", set_cookie),

    path("get_cookie/", get_cookie),

    path("set_session/", set_session),

    path("get_session/", get_session),

    # path的第一个参数是地址
    # path第二个参数是视图函数名
    path("login/", LoginView.as_view()),

    path("center/", CenterView.as_view()),

    path("demo/", demo),

    path("home/", HomeView.as_view()),

    path('zhuye/', ZY.as_view()),
]
