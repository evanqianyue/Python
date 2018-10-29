# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 17:15
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
值传递：传递的不可变类型
string,tuple,number
"""


def func1(num):
    print(id(num))
    num = 10
    print(id(num))  # 与其他不同


temp = 20
print(id(temp))
func1(temp)
print(temp)  # 20不变

"""
引用传递：传递的类型可变
list,dict,set是可变的
"""


def func2(list):
    print(id(list))
    list[0] = 100
    print(id(list))


list = [1, 2, 3]
print(id(list))
func2(list)
print(list)  # [100, 2, 3]


a = 10
b = 10
print(id(a), id(b))  # 相同
b = 15
print(id(a), id(b))  # 不同

