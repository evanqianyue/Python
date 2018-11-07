# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 22:59
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import time

time.clock()
sum = 0
for i in range(10000):
    sum += i
print(time.clock())
