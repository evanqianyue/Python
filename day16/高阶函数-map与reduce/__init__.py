# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/1 14:32
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

list1 = [1, 2, 3]
list2 = list1
list2[0] = 3
print(id(list1), id(list2))
print(list1, list2)
