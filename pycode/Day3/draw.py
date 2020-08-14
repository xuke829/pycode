#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/29 11:17
@Author  : Xuke
@File    : draw.py
"""
import turtle

t = turtle.Turtle(shape='turtle')
print('请问是画圆形还是等边三角形？')
print('圆形请按1，三角形请按2')
num = input()
num = int(num)
if num == 1:
    r = input('请输入半径：')
    r = int(r)
    print('是否需要填充颜色？  y/n')
    col = input()
    if col == 'y':
        co = input('请输入颜色')
        t.begin_fill()
        t.circle(r)
        t.color(co)
        t.end_fill()
    else:
        t.circle(r)
else:
    l = input('请输入边长')
    l = int(l)
    print('是否需要填充颜色？  y/n')
    col2 = input()
    if col2 == 'y':
        co2 = input('请输入颜色')
        t.begin_fill()
        t.color(co2)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.end_fill()
    else:
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
print('画图结束')

turtle.mainloop()
