# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 20:32
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
概念：是一个闭包，把一个函数当做参数传递返回一个替代版的函数
"""


# 简单的装饰器
def func1():
    print("he is good!")


def func2():
    print("she is good!")


def outer(func):
    def inner():
        print("************")
        func()

    return inner


# f是函数func1的加强版本
f = outer(func2)
f()
