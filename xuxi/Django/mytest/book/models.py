from django.db import models

# Create your models here.
'''
1、定义模型类
2、模型迁移
 2.1 先生成迁移文件（不会在数据库中生成表，只会创建一个数据表和模型的对应关系）
    python manage.py makemigratons
 2.2 再迁移（会在数据库中生成表）
    python manage.py migrate
3、操作数据库
（1）在哪里定义模型
（2）模型继承自谁就可以
（3）ORM对应的关系
    表-->类
    字段-->属性
'''
class BookInfo(models.Model):
    """
    1、主键    当前会自动生成
    2、属性    复制过来就可以

    """
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):

    name = models.CharField(max_length=10)
    # 性别
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


