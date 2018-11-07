# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 12:44
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
__init__()

# 如果不显示的写出构造函数，默认会自动添加一个空的构造函数

"""


class Person(object):

    def __init__(self, name, age, height, weight):
        # 定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # 定义方法, 第一个参数必须为self
    # self代表类的实例（某个对象）
    def run(self):
        print("I'm running")

    def eat(self, food):
        print("eat", food)


per = Person("Tom", 18, 170, 65)
per2 = Person("HMM", 16, 160, 45)
print(per.name, per.age, per.height, per.weight)
print(per2.name, per2.age, per2.height, per2.weight)
