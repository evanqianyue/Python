# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/5 14:56
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import requests
import json

response = requests.get("https://www.baidu.com", verify=False)

data = json.dumps(response.text)
print(type(data))
print(data)
