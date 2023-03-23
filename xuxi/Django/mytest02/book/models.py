from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # 属性名=属性类型（选项）
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')

    # 发布日期
    pub_data = models.DateField(null=True)

    # 阅读量
    readcount = models.IntegerField(default=0)

    # 评论量
    commentcount = models.IntegerField(default=0)

    # 是否删除
    is_delete = models.BooleanField(default=False)

    class Meta:
        # 改表名
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述')

    # on_delete
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='书籍')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # objects = models.Manager()


    class Meta:
        # 改表名
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

