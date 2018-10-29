# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 20:51
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)

    return inner


# 将装饰器运用到函数
@outer
def say(age):
    print("tom is %d years old" % age)


# say = outer(say)
say(-10)
