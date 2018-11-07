# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 17:19
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
对象属性的优先级高于类属性
"""


class Person(object):
    # 类属性
    name = "Evan"

    def __init__(self, name):
        # 对象属性
        self.name = name


print(Person.name)
p = Person("EEE")
# 动态的给对象添加对象属性
p.age = 18  # 只针对当前对象生效，对于类创建的其他对象没有作用
print(p.name, p.age)

# 删除对象中的name属性，再调用会使用同名的类属性
del p.name
print(p.name)

# 注意:以后不要将对象属性与类属性重名，因为对象属性会屏蔽掉类属性，但是删除对象属性后，再使用又能使用类属性
#
