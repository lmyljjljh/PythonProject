from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from book.models import BookInfo, PeopleInfo


def demo(request):
    return HttpResponse('demo')


def index(request):
    # 1、到数据库中查询书籍
    books = BookInfo.objects.all()

    # 2、组织数据
    context = {
        'books': books

    }
    # return render(request, 'index.html', context=context)
    # 跳转页面
    # path = reverse('book:index')
    # print(path)
    # return redirect('index/')
    # return redirect(path)

    return HttpResponse('index')


def detail(request, book_id, category_id):
    print(category_id, book_id)

    ############################跳转页面#########################################
    # path = reverse('book:index')
    # print(path)
    # return redirect('index/')
    # return redirect(path)

    ############################Get 传递参数#########################################
    # query_parmas = request.GET
    # # print(query_parmas)
    #
    # # <QueryDict: {'username': ['lmy'], 'password': ['123']}>
    # # QueryDict以普通字典形式来获取一键多值的时候只能获取最后那一个值
    # # 可以利用QueryDict的list方式
    # username = query_parmas['username']
    # password = query_parmas.get('password')
    # print(username, password)
    # users = query_parmas.getlist('username')
    # print(users)

    ############################Post表单 传递参数#########################################
    # data = request.POST
    # print(data)

    ############################Post   json数据#########################################
    # body = request.body
    # print(body.decode())  # Json形式的字符串
    # print(type(body.decode()))
    # # 转字符串
    # import json
    # # json.dumps()    # 将字典转换为 json形式的字符串
    # # json.loads()    # 将json形式的字符串转换为 字典
    # print(type(json.loads(body.decode())))

    ############################请求头#########################################
    # 系统请求头信息
    # print(request.META)
    # print("----------------------------------------------")
    # print(request.headers)
    # # 请求方式
    # print(request.method)

    ############################JsonResponse#########################################
    # data = {'name': 'lmy'}
    # return JsonResponse(data)
    ############################HttpResponse#########################################
    data = {'name': 'lmy'}
    # HttpResponse
    # content   传递字符串   不要传递    对象，字典等数据
    # status    响应状态码100-599只能使用系统的 "POST /detail/1/100/ HTTP/1.1" 400 6
    # content_type  是一个MIME类型
    #               语法形式时：大类/小类
    # text/html     text/css    text/javascript
    # application/json
    # Image/png     Image/gif   Image/jpeg
    return HttpResponse(data, status=400, content_type='application/json')


'''

保存在客户端的数据叫cookie
    0、概念
    1、流程（原理）
    2、效果
    3、从http协议角度深入掌握cookie的流程（原理）

保存在服务器端的数据叫session
    session需要依赖于cookie
    
    如果浏览器禁用了cookie，则session不能实现
    
    0、概念
    1、流程
        第一次请求：
            ①  我们第一次请求的时候可以携带一些信息（用户名/密码）cookie中没有任何信息
            ②  当我们的服务器接收到这个请求之后，进行用户名和密码的验证，验证没有问题可以设置session信息
            ③  在设置session信息的同时，服务器会在响应头中设置一个session id的cookie信息(由服务器端设置）
            ④  哭护短（浏览器）在接收到响应之后，会在cookie信息保存起来（保存   session id的信息）
        
        第二次请求及其之后的请求：
            ⑤  第二次及其之后的请求都会携带session id信息
            ⑥  当服务器接收到这个请求之后，会获取到session id信息，然后进行验证，
               验证成功，则可以获取  session信息（session 信息保存在服务器端）
    2、效果
    
    3、从原理（http）角度
'''


def set_cookie(request):
    # 1、先判断有没有cookie信息
    # 先假设就是没有

    # 2、获取用户名
    username = request.GET.get("username")
    # 3、因为我们假设没有cookie信息，我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')

    # key,value
    # max_age 单位是秒
    # 保存时间是 从服务器接受到这个请求时间 + 秒数  计算后的时间
    response.set_cookie('username', username, max_age=3600)

    # 删除cookie
    # 1、直接利用response的delete_cookie函数删除
    # response.delete_cookie('username')
    # 2、也可以利用set_cookie将max_age置为0即可
    # response.set_cookie('username', username, max_age=0)

    # 4、返回响应
    return response


def get_cookie(request):
    # 1、服务器可以接收（查看）cookie信息
    cookie = request.COOKIES
    # cookie 就是一个字典
    username = cookie.get('username')

    # 2、得到用户信息就可以继续其他的业务逻辑了

    return HttpResponse('get_cookie')

    pass


def set_session(request):
    # 1、
    print(request.COOKIES)
    # 2、对用户名和密码进行验证
    # 假设认为用户名和密码正确
    user_id = 666
    # 3、设置session信息
    # request.session   理解为字典
    # 设置session的时候其实做了2件事
    # 第一件：  将数据保存在数据库中
    # 第二件：  设置一个    cookie信息，这个cookie信息是以   session为key
    request.session['user_id'] = user_id

    # 4、返回响应
    return HttpResponse('set_session')


def get_session(request):
    # 1、请求都会携带session id信息
    print(request.COOKIES)

    # 2、会获取到sessionid信息，然后进行验证，
    #   验证成功，可以获取session信息（

    # request.session 字典
    user_id = request.session['user_id']
    user_id = request.session.get('user_id')

    # 3、返回响应

    return HttpResponse('get_session')


'''
登录页面
    GET 请求是获取登录的页面
    POST 请求是验证登录（用户名和密码是否正确）
'''


# GET 请求是获取登录的页面
def show_login(request):
    return render(request)


# POST 请求是验证登录（用户名和密码是否正确）
def veri_login(request):
    return redirect('首页')


# 我想由两个视图变为一个视图
def login(request):
    # 我们需要区分业务逻辑
    if request.method == 'GET':
        return render(request)
    else:
        return redirect('首页')


'''
面向对象
    类视图 是采用面向对象的思路
    
    1、定义类视图
        ① 继承自View（from django.view import View)
        ② 不同的请求方式有不同的业务逻辑
            类视图的方法就直接采用http的请求名字 作为我们的函数名，例如：get，post，put, delete
        ③ 类视图的方法的第二个参数 必须是请求实例对象
            类视图的方法必须有返回值返回值是HttpResponse及其子类
    2、类视图的url引导
'''

from django.views import View


class LoginView(View):
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')


'''
个人中心 -- 必须登录才能显示
GET 方式  展示  个人中心
POST 实现个人中心信息的修改
定义类视图
'''
from django.contrib.auth.mixins import LoginRequiredMixin


class CenterView(LoginRequiredMixin, View):

    def get(self):
        return HttpResponse("个人中心页面")

    def post(self):
        return HttpResponse("个人修改页面")


#######################################模板##########################################################

class HomeView(View):
    def get(self, request):
        # 1、获取数据
        username = request.GET.get('username')
        # 2、组织数据
        context = {
            'username': username,
            'age': 14,
            'firends': ['tom', 'jack', 'rose'],
            'birthday': datetime.now(),
            'money': {
                '2019': 12000,
                '2020': 18000,
                '2021': 25000,
            },
            'desc': '<script>alert("hot")</script>',


        }

        return render(request, 'index.html', context=context)

class ZY(View):
    def get(self, request):

        return render(request, 'detail.html')

