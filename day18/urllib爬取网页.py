# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/5 14:56
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import urllib.request



response = urllib.request.urlopen("https://www.baidu.com")


data = response.read().decode("utf-8")

print(data)
