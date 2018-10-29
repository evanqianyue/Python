# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/27 19:12
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import random

num = input("请输入1-10的任意号码：")

r2 = random.choice(range(10))+1
# 判断是否中奖
print(r2)
print(num)
if num is not None:
    if num == str(r2):
        print("中奖啦！")
    else:
        print("未中奖")

