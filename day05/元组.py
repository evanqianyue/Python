# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 12:31
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

# 元组不可变,安全！！！！
# 修改元组
tuple5 = (1, 2, 3, 4, [5, 6, 7])
tuple5[4][1] = 8
print(tuple5)

# 二位元组
tuple6 = ((1, 2), (2, 3))
print(tuple6)

# 元组方法
# len()
# max()
# min()
# tuple(list)
list2 = [123]
list3 = tuple(list2)
print(type(list3))

#