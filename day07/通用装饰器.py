# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 21:08
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


def outer(func):
    def inner(*args, **kwargs):
        # 添加修改功能
        print("############")
        func(*args, **kwargs)

    return inner


@outer
def say(name, age):
    print("my name is %s,my age is %d" %(name, age))

say("evan", 18)
