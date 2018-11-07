# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 16:27
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
"""
多态：一种事物的多种状态
"""


from cat import Cat
from mouse import Mouse
from person import Person


tom = Cat("Tom")
jerry = Mouse("Jerry")
tom.eat()
jerry.eat()
p = Person()
p.feedAnimal(tom)

