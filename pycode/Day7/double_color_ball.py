#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/4 15:33
@Author  : Xuke
@File    : double_color_ball.py
"""
import random

a = []
for i in range(64):
    a.append(i + 1)
print(random.choices(a, k=5))
