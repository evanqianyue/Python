# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 13:17
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import requests
import json

for i in range(0, 11):
    response = requests.get(
        "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=" + str(
            i * 10) + "&limit=20",
        verify=False).json()

    print(i, response)
