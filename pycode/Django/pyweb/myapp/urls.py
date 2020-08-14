#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/14 18:17
@Author  : Xuke
@File    : urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello),
    path('', views.index),
    path('add', views.add_data),
]