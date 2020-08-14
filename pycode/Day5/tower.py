#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/1 16:16
@Author  : Xuke
@File    : tower.py
"""

bl = True
while bl:
    height = input('请输入塔的高度：')
    height = int(height)
    if height < 0:
        print('输入错误：请输入0-10以内的数！')
    elif height < 11:
        for i in range(height):
            print('{:^20}'.format('='*(2*i+1)))
        bl = False
    elif height > 11:
        print('输入错误：请输入0-10以内的数！')