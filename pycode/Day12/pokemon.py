#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/10 17:03
@Author  : Xuke
@File    : pokemon.py
"""


class Pokemon:

    def __init__(self, name):
        self.name = name


class Water(Pokemon):
    def say(self):
        print(self.name + ' 水属性' + '技能：水龙弹')


class Fire(Pokemon):
    def say(self):
        print(self.name + ' 火属性' + '技能：火龙炎弹')


class Grass(Pokemon):
    def say(self):
        print(self.name + ' 草属性' + '技能：草龙弹')


class Jng(Water):
    pass


class Xhl(Fire):
    pass


class Mwzz(Grass):
    pass


j = Jng('杰尼龟')
x = Xhl('小火龙')
m = Mwzz('妙蛙种子')
j.say()
x.say()
m.say()
