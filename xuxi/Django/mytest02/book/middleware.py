"""
中间件的作用：每次请求和响应都会调用
中间件的定义

中间件的使用：如果有多次需要判断或请求的我们可以使用中间件
"""
from django.http import HttpResponse


def simple_middleware(get_response):
    def middleware(request):
        # username = request.COOKIE.get('username')
        # if username is None:
        #     print("username is None")
        #     return HttpResponse("未登录")
        # 这里是请求前
        print('before request')
        response = get_response(request)
        # 这里是响应后/请求后
        print('after response')

        return response

    return middleware
