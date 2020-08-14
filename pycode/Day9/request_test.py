#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/6 10:11
@Author  : Xuke
@File    : request_test.py
"""

import requests
import re

s = ''
a = ''
with open('repose_1.html', 'r', encoding='utf-8') as f:
    s = f.read().replace('\n', '').replace('\t', ' ')
pa = re.compile(r'<a class="name"[\s\S]*?>([\s\S]+?)</a>')
result = pa.findall(s)
pa2 = re.compile(r'<span class="time-since"[\s\S]*?>([\s\S]*?)</span>')
result2 = pa2.findall(s)

for i, j in zip(result, result2):
    a = a+i+j + '\n'
print(a)

