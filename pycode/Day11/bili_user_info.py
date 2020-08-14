#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/8 9:43
@Author  : Xuke
@File    : bili_user_info.py
"""

import requests
import re
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' + 'AppleWebKit/537.36 (KHTML, like Gecko)' +
                  'Chrome/81.0.4044.138 Safari/537.36'
}


def pa(url):
    t = requests.get(url, headers=headers)
    text = t.text
    pa_name = re.compile(r'"name":"([\s\S]*?)",')
    pa_mid = re.compile(r'"mid":([\s\S]*?),')
    pa_sign = re.compile(r'"sign":"([\s\S]*?)",')
    pa_level = re.compile(r'"level":([\s\S]*?),"jointime":0')
    mid = ''.join(pa_mid.findall(text))
    name = ''.join(pa_name.findall(text))
    sign = ''.join(pa_sign.findall(text))
    level = ''.join(pa_level.findall(text))
    result = mid + ',' + name + ',' + sign + ',' + level + '\n'
    return result


def write(file):
    with open('result.csv', 'a+', encoding='utf-8') as f:
        f.write(file)


def clean():
    with open('result.csv', 'w+', encoding='utf-8') as f:
        f.write('')


def main():
    clean()

    for i in range(1, 51):
        url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(i)
        write(pa(url))
        time.sleep(1)


main()
