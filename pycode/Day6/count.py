#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/2 15:38
@Author  : Xuke
@File    : count.py
"""

f = open('TheOldManAndtheSea.txt', 'r', encoding='UTF-8')
text = f.read().lower()   # 将所有单词转换为小写
result = {}        # 创建一个空字典 存放单词和其出现的次数
temp = ''           # 创建一空字符串 存放单词 以及当前字符
flag = False        # 判断单词是否结束
Max = 0             # 存放最大值
for i in text:
    if 'a' <= i <= 'z':             # 判断是不是字母
        temp = temp + i             # 如果是字母 存放到temp
        flag = False                # 如果下一个还是字母单词未取完 则不能存放字典里
    else:
        t = temp                    # 将前面的字符串暂存 用于判断单词是否完整 存放上一个单词
        temp = ''                   # 如果不是字母 字符串置空
        flag = True                 # 出现了不是字母的字符 表示前面一个单词完全取出 flag = true进入下面存放
    if flag and t != '':            # 当出现不是字母的字符，并且前面一个字符串为单词时进入
        if t not in result:         # 判断字典里是否有此单词
            result[t] = 1           # 无 则数值置1
        else:                       # 否则就原数值加1
            result[t] = result[t] + 1
print(result)
for key, value in result.items():
    Max = max(Max, value)           # 找出最大值
for i in result:
    if result[i] == Max:            # 找出最大值对应的单词写入out.txt
        print(i)
        out = open("out.txt", 'w+', encoding='utf-8')
        out.write(i)
        out.close()
f.close()
