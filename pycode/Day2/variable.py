#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/28 14:30
@Author  : Xuke
@File    : variable.py
"""
num1 = input('请输入num1的值：')     # input内的字符会在print之前先打印出来
num1 = int(num1)    # 强制转换 input 输入是字符串类型type()函数可以查看数据类型
num2 = input('请输入num2的值')
num2 = int(num2)

print('num1+num2=', num1 + num2)
print('num1-num2=', num1 - num2)
print('num1*num2=', num1 * num2)
print('num1/num2=', num1 / num2)
