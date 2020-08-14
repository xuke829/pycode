#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/2 15:48
@Author  : Xuke
@File    : passwd.py
"""

psd = open('password.txt', 'r+', encoding='UTF-8')
t = psd.read()
d = ''            # 存放解密后的字符串

for i in t:
    if ord(i) in range(97, 123):   # 判断字符是否为26字母
        j = chr(ord(i) + 2)        # 是则解密 +2
        if ord(j) > 122:
            j = chr(ord(j) - 26)   # 超过z的从a开始
        d = d + j
    else:
        d = d + i

print(d)

psd.close()
