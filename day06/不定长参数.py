# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 19:33
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


# 能处理比定义时更多的参数
# 加了星号(*)的变量，会存放所有未命名的变量参数,若没有则为空数组

def func(name, *args):
    print("name:", name)
    for x in args:
        print(x)


func("1", "2", "3", "4")


def mySum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(mySum(1, 2, 3, 4, 5))


# print(mySum(1, 2, 3, 4, "a")) TypeError: unsupported operand type(s) for +=: 'int' and 'str'


# ** 代表键值对的参数字典，和*所代码的意思类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))


func2(x=1, y=2, z=3)


def func3(*args, **kwargs):
    pass

