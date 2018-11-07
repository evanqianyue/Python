# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 11:25
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import pickle  # 数据持久性模块
import json

myList = [1, 2, 3, 4, 5, "he is good"]

with open(r"D:\file\write2.txt", "wb") as f:
    pickle.dump(myList, f)

with open(r"D:\file\write2.txt", "rb") as f:
    print(pickle.load(f))

myDict = {"1": 2, "3": "4"}
str = json.dumps(myDict)
print(str)
with open(r"D:\file\write3.txt", "w+") as f:
    f.write(str)

