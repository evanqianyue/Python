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
import re
import time

for i in range(1, 5):
    print("pageNumber:%d" % i)
    response = requests.get(
        "https://www.qiushibaike.com/text/page/" + str(i) + "/",
        verify=False)
    print(response.text)
    content = re.findall(r'<div class="content">\n<span>(.*?)</span>', response.text, re.S)
    for j in range(0, len(content)):
        # print("jokeNumber:", j, "\n", content[j].strip("\n").replace("<br/>", ""), "\n")

        print("jokerNumber:%d\n%s\n" % (j, content[j].strip("\n").replace("<br/>", "")))
