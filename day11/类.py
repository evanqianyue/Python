# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 10:37
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
设计原则
类名：见名之意，首字母大写，遵循驼峰原则
属性：见名之意，遵循驼峰原则
行为：见名之意，遵循驼峰原则
"""


# object:基类，超类，所有类的父类
# 没有合适的父类就写object
class Person(object):
    name =""
    age = 0
    height = 0
    weight = 0

    # 定义方法, 第一个参数必须为self
    # self代表类的实例（某个对象）
    def run(self):
        print("I'm running")

    def eat(self, food):
        print("eat", food)

