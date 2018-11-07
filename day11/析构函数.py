# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 13:00
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
__del__()  析构函数，释放对象时使用

"""


class Person(object):

    def __init__(self, name, age, height, weight):
        # 定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    #
    def say(self):
        print("My name is %s,I'm %d years old" %(self.name, self.age))

    # 定义方法, 第一个参数必须为self
    # self代表类的实例（某个对象）
    def run(self):
        print("I'm running")

    def eat(self, food):
        print("eat", food)

    def __del__(self):
        print("this is 析构函数!")


per = Person("Tom", 18, 170, 65)
del per

# 在函数里定义的对象，会在函数结束时自动释放，这样可以用来减少内存空间的浪费
def fun():
    per2 = Person("Tom2", 18, 170, 65)

fun()

