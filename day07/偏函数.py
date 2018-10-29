# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 21:44
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
import functools

print(int("1010", base=2))
int3 = functools.partial(int, base=2)
print(int3("111"))
