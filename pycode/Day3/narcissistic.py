#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/29 14:58
@Author  : Xuke
@File    : narcissistic.py
"""
count = 0
for i in range(100, 1000):
    t = i
    a = int(t / 100)
    b = int((t / 10) % 10)
    c = int(t % 10)

    if t == a ** 3 + b ** 3 + c ** 3:
        count = count + 1
        print(i)
print('count = ', count) 
