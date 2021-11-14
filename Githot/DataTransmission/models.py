from django.db import models


# Create your models here.
# TODO 2.数据库设计，使用ORM设计五个表
class User(models.Model):
    '''用户类'''
    wx_id = models.CharField(max_length=50, primary_key=True)  # 微信id
    # name = models.CharField(max_length=10)  # 用户昵称
    # img = models.ImageField()  # 用户头像
    collections = models.JSONField(null=True)  # 用户收藏
    readHistory = models.JSONField(null=True)  # 用户阅读记录


class Project(models.Model):
    '''收藏项目类'''
    id = models.UUIDField(primary_key=True)  # UUID
    link = models.URLField()  # 链接
    key_words = models.JSONField  # 项目关键词
    project_type = models.IntegerField()  # 项目分类


class HotList_Day(models.Model):
    '''热度日榜单'''
    date = models.DateField(primary_key=True)  # 日期
    rank = models.JSONField()  # 排行


class HotList_Week(models.Model):
    '''热度周榜单'''
    date = models.DateField(primary_key=True)  # 日期
    rank = models.JSONField()  # 排行


class HotList_Month(models.Model):
    '''热度月榜单'''
    date = models.DateField(primary_key=True)  # 日期
    rank = models.JSONField()  # 排行


class HotList_Year(models.Model):
    '''热度年榜单'''
    date = models.DateField(primary_key=True)  # 日期
    rank = models.JSONField()  # 排行

# $ python3 manage.py migrate   # 创建表结构
#
# $ python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
# $ python3 manage.py migrate TestModel   # 创建表结构
