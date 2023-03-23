from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from book.models import BookInfo

# Create your views here.
'''
视图 
1、就是python函数
2、函数的第一个参数就是请求  和请求相关的  它是HttpRequest的实例对象
3、我们必须要返回一个响应 响应是HttpResponse的实例对象/子类实例对象
'''


def index(request):
    name = '小姐姐'
    # request, template_name, context=None
    # 参数1：当前的请求
    # 参数2：模板文件
    # 实现业务逻辑
    # 1、先把所有书籍查询出来
    # select * from bookinfo
    # ORM
    books = BookInfo.objects.all()
    # 组织数据
    context = {
        'books': books,
        'name': name
    }
    return render(request, 'index.html', context=context)
    return HttpResponse('index')
