# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 13:08
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
将函数定义重新写一遍

__str__():在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
当一个对象的属性很多，并且需要打印时，重写__str__()

__repr__():给机器用的，在python解释器里面直接敲对象名再回车

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
        print("My name is %s,I'm %d years old" % (self.name, self.age))

    # 定义方法, 第一个参数必须为self
    # self代表类的实例（某个对象）
    def run(self):
        print("I'm running")

    def eat(self, food):
        print("eat", food)

    def __str__(self):
        return "person:%s %d %d %d" % (per.name, per.age, per.height, per.weight)


per = Person("Tom", 18, 170, 615)
print(per)
