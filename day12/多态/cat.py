# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 16:25
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from animal import Animal


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
