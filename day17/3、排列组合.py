# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/1 20:31
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import itertools

myList = list(itertools.product([1, 2, 3, 4], repeat=3))

print(myList)
print(len(myList))