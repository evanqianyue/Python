# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 15:37
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from person import Person


class Student(Person):
    def __init__(self, name, age, stuId):
        super().__init__(name, age)
        # 子类可以有自己的属性
        self.stuId = stuId


stu = Student("Tom", 20, 1003)
print(stu.stuId)