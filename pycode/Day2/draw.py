#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/28 15:25
@Author  : Xuke
@File    : draw.py
"""
import turtle

# 创建一个画笔对象 形状为海龟
t = turtle.Turtle(shape='turtle')

c = input('请输入等边三角形的边长')
r = input('请输入圆的半径')
c = int(c)
r = int(r)
t.penup()
t.goto(200, 200)
t.pendown()
t.forward(c)  # 让海龟朝头的方向移动
t.left(120)
t.forward(c)
t.left(120)  # 让海龟向右旋转 t.left()左转
t.forward(c)

t.penup()
t.home()
t.right(90)
t.forward(r)
t.left(r)
t.pendown()
t.circle(r)


"""
t.forward(100)   # 让海龟朝头的方向移动
t.left(120)
t.forward(100)      
t.left(120)          # 让海龟向右旋转 t.left()左转
t.forward(100)

t.penup()   # 海龟起飞 移动的时候不会有痕迹
t.pendown()  # 海龟降落 留下痕迹
t.reset()    # 回到初始位置 并清除痕迹
t.home()     # 移动到最开始的位置 不清除痕迹
t.goto()      # 移动到指定坐标
t.circle()     # 画一个指定半径的圆
t.hideturtle()  # 海龟隐身
t.showturtle()  # 海龟现身
t.forward(100)   # 让海龟朝头的方向移动
t.right(144)
t.forward(100)
t.right(144)
t.forward(100)
t.right(144)
t.forward(100)
t.right(144)
t.forward(100)
"""
# 持续刷新窗口
turtle.mainloop()
