# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/1 15:28
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


# python内置map() 和 reduce()

# map(fn，lsd)
# fn是函数，lsd是序列

# 功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回

def char2int(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3}[chr]


myList = ["2", "3", "0"]

res = map(char2int, myList)
print(res)
print(list(res))

