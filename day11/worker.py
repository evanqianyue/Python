# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 15:43
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from person import Person


class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def run(self):
        print("I'm running")

    def eat(self, food):
        print("eat", food)


wo = Worker("te", 30)
print(wo.name)
wo.eat("banana")

