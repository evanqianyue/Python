# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/27 16:47
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
age = 12
age = 19
# 查看变量类型
print(type(age))
# 查看变量地址
print(id(age))

print(age)
del age

print(3/2)
# print(age) # 这个会报错


num_1 = int(input("请先输入一个数字:"))
num_2 = int(input("请再输入一个数字:"))

print("num_1 + num_2 =", num_1+num_2)
