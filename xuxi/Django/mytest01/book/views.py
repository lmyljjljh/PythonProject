from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo, PeopleInfo


def index(request):
    # 1、到数据库中查询书籍
    books = BookInfo.objects.all()

    # 2、组织数据
    context = {
        'books': books

    }
    return render(request, 'index.html', context=context)
    return HttpResponse('index')


'''
类似于ipython的东西
python manage.py shell
'''
##############################插入数据#######################################

# 方式1 需要手动调用save方法
# 会把新生成的对象返回给我们
# from book.models import BookInfo
# t1 = BookInfo(
#     name='python',
#     pub_data='2000-01-01',
# )
#
# t1.save()
#
# # 方式2 直接入库
# # objects 模型的管理类
# # 我们对模型的增删改查 都找它
# BookInfo.objects.create(
#     name='jave',
#     pub_data='2010-01-01'
# )

##############################修改（更新）数据#######################################

# from book.models import BookInfo
#
# # 方式一
# # 1、先查询数据
# # select * from bookinfo where id=1
# t2 = BookInfo.objects.get(id=1)
#
# # 2、修改数据：直接修改实例的属性
# t2.readcount = 20
#
# # 3、保存数据
# t2.save()
#
# # 方式二
# BookInfo.objects.filter(id=1).update(
#     readcount=100,
#     commentcount=200
# )


##############################删除数据#######################################

# from book.models import BookInfo
# # 方式一 直接删除不需要保存
# # 1、先查询出数据
# t = BookInfo.objects.get(id=5)
#
# # 2、调用删除方法
# t.delete()
#
# # 方式二
# BookInfo.objects.filter(id=6).delete()


##############################查询数据#######################################

# get 得到某一个数据
# all 获得所有的
# count 个数

# select * from bookinfo where id=1
# 返回一个对象
# t = BookInfo.objects.get(id=1)
# # 查询id 不存在的数据会抛出异常
# """
# DoesNotExist: BookInfo matching query does not exist.
# """
# # 返回所有结果，列表
# BookInfo.objects.all()
#
# # count
# BookInfo.objects.all().count()
# BookInfo.objects.count()


# ##############################filter, get, exclude#######################################
#
# '''
# # select * from bookinfo where 条件语句
# 相当于 where查询
# filter              ：筛选/过滤 返回 n个结果（n=0/1/n）
# get                 ：         返回1个结果
# exclude             ： 排除掉符合条件剩下的结果      相当于not
# 语法形式：
#     以filter为例：（字段名__运算符=值）
# # 查询编号为1的图书
# # 查询书名包含'湖'的图书
# # 查询书名以'部'结尾的图书
# # 查询书名为空的图书
# # 查询编号为1或3或5的图书
# # 查询编号大于3的图书
# # 查询1980年发表的图书
# # 查询1990年1月1日后发表的图书
# '''
# # 查询编号为1的图书 get 返回的是一个对象 filter返回的是一个‘列表’
# BookInfo.objects.get(id__exact=1)
# BookInfo.objects.get(id=1)
#
# BookInfo.objects.filter(id__exact=1)
# BookInfo.objects.filter(id=1)
# # 查询书名包含'湖'的图书
# BookInfo.objects.filter(name__contains='湖')
# # 查询书名以'部'结尾的图书
# BookInfo.objects.filter(name__endswith='部')
# # 查询书名为空的图书
# BookInfo.objects.filter(name__isnull=True)
# # 查询编号为1或3或5的图书
# BookInfo.objects.filter(id__in=[1, 3, 5])
# # 查询编号大于3的图书    gt-->great大的 gte-->大于等于 lt-->小于 lte-->小于等于
# BookInfo.objects.filter(id__gt=3)
# # 查询编号不为3的图书
# BookInfo.objects.exclude(id=3)
# BookInfo.objects.exclude(id__exact=3)
# # 查询1980年发表的图书
# BookInfo.objects.filter(pub_data__year='1980')
# # 查询1990年1月1日后发表的图书
# BookInfo.objects.filter(pub_data__gt='1990-01-01')
#
# ##############################F对象#######################################
#
# '''
# F对象的语法形式
#
# filter(字段名__运算符=F('字段名')
#
# 查询阅读量大于等于评论量的图书
# '''
# from django.db.models import F
#
# # 查询阅读量大于等于评论量的图书
# BookInfo.objects.filter(readcount__gte=F('commentcount'))
#
# # 查询阅读量大于等于评论量2倍的图书
# BookInfo.objects.filter(readcount__gte=F('commentcount') * 2)
#
# ##############################Q对象#######################################
#
# # 需要查询id大于2并且阅读量大于20的书籍
#
# # 方式一
# BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)
#
# # 方式二
# BookInfo.objects.filter(id__gt=2, readcount__gt=20)
#
# # 需要查询id大于2或者阅读量大于20的书籍
# from django.db.models import Q
#
# """
# Q(字段名__运算符=值)
#
# 或   Q()|Q() ..
# 并且 Q()&Q()
# not ~Q()
# """
# BookInfo.objects.filter(Q(id__gt=2) | Q(readcount__gt=20))
#
# # 查询编号不为3的图书
# BookInfo.objects.filter(~Q(id=3))
#
# ##############################聚合函数（了解）#######################################
#
# '''
# Sum,Max,Min,Avg,Count
#
# 聚合函数需要使用    aggregate
# 语法形式是：aggregate(Xxx('字段'))
#
# '''
# # 当前书籍的阅读总量
# from django.db.models import Sum, Avg, Min, Max, Count
#
# BookInfo.objects.aggregate(Sum('readcount'))
#
# ##############################排序#######################################
#
# # 默认升序
# BookInfo.objects.all().order_by('readcount')
#
# # 降序
# BookInfo.objects.all().order_by('-readcount')
#
# ##############################关联查询#######################################
#
# '''
#
# 书籍和人物的关系是一对多
# 书籍中没有任何人物的字段
#
# 人物中有关于书籍的字段 book 字段
#
# 语法形式
#     通过书籍查询人物信息（已知主表信息，关联查询从表数据）
#     主表模型，关联模型类名小写_set
#
#     通过人物查询书籍信息（已知从表数据，关联查询主表数据）
#     从表模型（实例对象），外键
#
# '''
#
# # 查询书籍为1的人物信息
#
# # 通过书籍 查询人物
#
# # 1、查询书籍
# book = BookInfo.objects.get(id=1)
# # 2、根据书籍关联人物信息
# book.peopleinfo_set.all()
#
# # 查询人物为1的书籍信息
# # 1、查询人物
# person = PeopleInfo.objects.get(id = 1)
# # 2、根据人物关联查询书籍
# person.book
# person.book.name
#
#
# ##############################关联查询的筛选#######################################
#
# '''
# 书籍和人物的关系是 1：n
# 书籍中没有任何人物的字段
#
# 人物中有关于书籍的字段 book 字段
#
# 语法形式
#     我们需要的是  书籍信息，已知条件是人物信息
#     我们需要的是  主表数据，已知条件是从表信息
#
#     我们需要的是  人物信息，已知条件是书籍信息
#     我们需要的是  从表数据，已知条件是主表信息
# '''
#
# # 1、查询图书，要求图书人物为“郭靖”
# BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
# BookInfo.objects.filter(peopleinfo__name='郭靖')
#
# # 2、查询图书，要求图书人物的描述包含“八”
# BookInfo.objects.filter(peopleinfo__description__contains='八')
#
# # 3、查询书名为“天龙八部”的所有人物
# PeopleInfo.objects.filter(book__name='天龙八部')
# PeopleInfo.objects.filter(book__name__exact='天龙八部')
#
# # 4、查询图书阅读量大于30的所有人物
# PeopleInfo.objects.filter(book__readcount__gt=30)

##############################查询集Queryset#######################################

# [book.id for book in BookInfo.objects.all()]
# 无缓存
# 利用变量赋值就可避免

##############################分页#######################################

# from django.core.paginator import Paginator
# book = BookInfo.objects.all()
# # object_list   结果集/列表
# # per_page      每页多少条记录
#
# p = Paginator(book, 2)
#
# # 获取第几页的数据
# books_page=p.page(1)

