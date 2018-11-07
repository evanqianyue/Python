# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 13:22
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


class Person(object):
    __money = 0

    def __init__(self, name, age, height, weight, money):
        # 定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money

    #
    def setMoney(self, money):
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money

    def say(self):
        print("My name is %s,I'm %d years old" % (self.name, self.age))

    # 定义方法, 第一个参数必须为self
    # self代表类的实例（某个对象）
    def run(self):
        print("I'm running")

    def eat(self, food):
        print("eat", food)

    def __str__(self):
        return "person:%s %d %d %d %d" % (per.name, per.age, per.height, per.weight, per.__money)


per = Person("Tom", 18, 170, 65, 20)

# 如果要让内部的属性不被外部直接访问，在属性前加2个下划线变为私有属性

# print(per.__money)  # 'Person' object has no attribute '__money'
per.setMoney(2000)
print(per.getMoney())
print(per)


