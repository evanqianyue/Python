# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 18:37
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


class Person(object):
    def __init__(self, age):
        # 属性直接对外暴露
        # self.age = age
        # 限制访问
        self.__age = age

    '''
    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age < 0:
            age = 0
        self.__age = age
    '''

    # 方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age

    @age.setter  # 去掉下划线.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age


# 不安全，没有数据过滤
per = Person(18)
per.age = 30

print(per.age)

# 使用限制访问，需要自己set和get方法


