#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 下午5:59
# @Author  : CoderP
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]