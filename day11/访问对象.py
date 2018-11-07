# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 12:38
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from 类 import Person

per = Person()

per.name = "Tom"
per.age = 18
per.height = 170
per.weight = 60
print(per.name)
print(per.age)
print(per.height)
print(per.weight)

per.run()
per.eat("apple")


per3 = Person()


print(per3.name)
print(per3.age)
print(per3.height)
print(per3.weight)
