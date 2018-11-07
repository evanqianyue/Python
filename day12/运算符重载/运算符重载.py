# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/1 13:11
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


#

class Person():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Person(self.num + other.num)

    def __str__(self):
        return ("num=" + str(self.num))


per1 = Person(10)
per2 = Person(20)
print(per1 + per2)
