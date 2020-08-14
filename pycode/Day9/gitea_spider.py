#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/6 10:54
@Author  : Xuke
@File    : gitea_spider.py
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
                  ' AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/81.0.4044.138 Safari/537.36'
}
for i in range(1, 4):

    r = requests.get('http://gitea.boulderh.top/explore/repos?page={}&sort=recentupdate&q=&topic=false'.format(i),
                     headers=headers)
    f = open('repose_{}.html'.format(i), 'w+', encoding='utf-8')
    f.write(r.text)
    f.close()