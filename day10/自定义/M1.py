# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 8:19
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


def sayGood():
    print("sayGood")

def sayHello():
    print("Hello")

TT = 100

# 每一个模块都有一个__name__属性, 当其值等"__main__"，表面该模块自身在执行。
if __name__ == "__main__":
    print("M1!!")

else:
    print("******"+__name__)