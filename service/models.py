from django.db import models
from django import forms

# Create your models here.


class Chess(models.Model):
    turn = models.CharField(max_length=10)
    diff = models.IntegerField()
    win = models.BooleanField()
    list = models.CharField(max_length=1000)

    # def __init__(self, *args):
    #     super(Chess, self).__init__(*args)

    class Meta:
        verbose_name_plural = 'chess'
