#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/4 16:11
@Author  : Xuke
@File    : double_color_ball2.py
"""
import random
import time

a = []
for i in range(64):
    a.append(i + 1)

name = time.strftime('%Y-%m-%d', time.localtime())

result = open(name, 'w+', encoding='UTF-8')
result.write(str(random.choices(a, k=5)))
result.close()