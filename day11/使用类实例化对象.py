# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 11:25
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

class Person(object):
    name =""
    age = 0
    height = 0
    weight = 0

    def run(self):
        print("run")

    def eat(self, food):
        print("eat", food)

"""
格式： 对象名 = 类名（参数列表）
注意： 没有参数，小括号也不能省略
"""

per1 = Person()
print(per1)      # 显示的是二进制地址
print(id(per1))  # 显示十进制地址

per2 = Person()
print(per2)      # 显示的是二进制地址
print(id(per2))  # 显示十进制地址
