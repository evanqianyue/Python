# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 16:29
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name+"吃")


