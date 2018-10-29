# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/28 21:54
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


# range() 列表生成器
for i in range(0, 20, 2):
    print(i)

# 同时便利下标和元素
for index, num in enumerate(range(0, 20, 2)):
    print(index, num)

# break
for i in range(5):
    print(i)
    break

# continue
for i in range(5):
    if i == 1:
        continue
    print(i)
