# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 19:59
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""

"""


def product(c):
    c.send(None)
    for i in range(5):
        print("P生产者产生数据%d" % i)
        r = c.send(str(i))
        print("P消费者数据%s" % r)
    c.close()


def customer():
    data = ""
    while True:
        r = yield data
        if not r:
            print("None")
            return
        else:
            print("C消费者消费了%s" % r)
        data = "200"


c = customer()
print("product(c)")
product(c)
