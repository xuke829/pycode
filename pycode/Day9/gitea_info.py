#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/6 15:52
@Author  : Xuke
@File    : gitea_info.py
"""

import re
import requests


def get_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
                      ' AppleWebKit/537.36 (KHTML, like Gecko) ' +
                      'Chrome/81.0.4044.138 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text.replace('\n', '').replace('\t', '')
    else:
        print('访问错误！')


def write_result(file):
    with open('out.txt', 'w+', encoding='utf-8') as f:
        f.write(file)


def match(files):
    result = ''
    pa1 = re.compile(r'<a class="name"[\s\S]*?>([\s\S]*?)</a>')
    result1 = pa1.findall(files)
    pa2 = re.compile(r'<span class="time-since"[\s\S]*?>([\s\S]*?)</span>')
    result2 = pa2.findall(files)
    for i, j in zip(result1, result2):
        result = result + i + j + '\n'
    return result


def main():
    total = ''
    for i in range(1, 4):
        url = 'http://gitea.boulderh.top/explore/repos?page={}&sort=recentupdate&q=&topic=false'.format(i)
        text = get_info(url)
        result = match(text)
        total = total + result
    print('完成！')
    write_result(total)


main()