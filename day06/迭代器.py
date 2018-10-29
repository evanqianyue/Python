# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 16:27
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
from collections import Iterable
from collections import Iterator

"""
迭代器：不但可以用作于for循环，还可以被next（）函数不断调用并返回下一个值，
知道最后跑出一个StopIteration错误表示无法继续返回下一个值

凡是可作用于for循环的对象都是Iterable类型；
凡是可用作next()函数的对象都是Iterator类型，它表示一个惰性计算的序列。
集合数据类型如list，dict，str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

"""
# 可以用isinstance判断是否是Iterable
print(isinstance([], Iterable))
print(isinstance([], list))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))

#
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((), Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))

l = (x for x in range(5))
print(l)  # <generator object <genexpr> at 0x0000000002E4E7E0>
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
# print(next(l))  # StopIteration

# 转成Iterator 对象
a = iter([1, 2, 3, 4])
print(next(a))

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter(""), Iterator))