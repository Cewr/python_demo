from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):  # Model 继承一个 Django 中定义了模型基本功能的类
    '''学习主题'''
    text = models.CharField(max_length=200)  # CharField 字符或文本组成的数据
    # DateTimeField 记录时间数据，auto_now_add 创建时自动设置成当前时间
    date_added = models.DateTimeField(auto_now_add=True)
    # 建立到模型 User 的外键关系
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):  # py2.7 应调用 __unicode__()
        '''返回模型的字符串表示'''
        return self.text

    class Meta:
        # verbose_name = '主题'
        verbose_name_plural = '主题'


class Entry(models.Model):
    '''学到有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '主题详情'

        def __str__(self):
            '''返回模型的字符串表示'''
            return self.text[:50] + '...'
