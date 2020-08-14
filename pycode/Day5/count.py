#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/1 9:51
@Author  : Xuke
@File    : count.py
"""
s = input('请输入一个字符串：')
s = list(s)
ss = {}
for i in range(len(s)):
    j = i + 1
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1
    ss[s[i]] = count
for key, value in ss.items():
    print(key, value)
