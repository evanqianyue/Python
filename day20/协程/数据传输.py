# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 19:50
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


def run():
    # 空变量，存储的作用data始终为空
    data = ""
    r = yield data

    # r=a
    print(1, r, data)
    r = yield "aa"

    # r=b
    print(2, r, data)
    r = yield "bb"

    # r=c
    print(3, r, data)
    r = yield "cc"


m = run()
print(m.send(None))
print(m.send("a"))
print(m.send("b"))
print(m.send("c"))


print("*****")
