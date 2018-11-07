# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 18:29
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
from types import MethodType


#
class Person(object):
    __slots__ = ("na1me", "age", "speak")
    pass


per = Person()

per.name = "Tom"


# 动态添加方法
def say(self):
    print("my name is " + self.name)


per.speak = MethodType(say, per)

per.speak()

# 限制实例的属性
# 在定义类的时候定义一个特殊的属性__slots__
