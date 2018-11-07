# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 19:44
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
python对协程的支持是通过generator实现的

"""


def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30


# 协程最简单的风格，控制函数的阶段执行，节约线程或者进程的切换
# 返回的是生成器  , m 是生成器
m = run()
print(type(m))
print(next(m))
