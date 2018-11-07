# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 12:52
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
self代表类的实例，而非类
哪个对象调用方法，那么该方法的self就代表那个对象
self.__class__ 代表类名

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


per = Person("Tom", 18, 170, 65)
per2 = Person("HMM", 16, 160, 45)
per.say()
per2.say()

