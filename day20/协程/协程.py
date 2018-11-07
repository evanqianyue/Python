# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 19:30
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
子程序/子函数：
在所有语言中都是层级调用，比如A调用B，在B执行的过程中，又可以调用C，C执行完毕返回，B执行完毕返回，最后是A执行完毕.
是通过 栈 实现。一个线程就是执行一个子程序，子程序调用总是一个入口，一次返回。

协程概述：
看上去是子程序，但执行过程中，在子程序的内部可中断，然后转而去执行别的子程序，不是函数调用。

协程执行效率极高，因为只有1个线程，也不存在同时写变量的冲突，在协程中共享资源不加锁，只需要判断状态

"""


def C():
    print("C-Start")

    print("C-End")


def B():
    print("B-Start")
    C()
    print("B-End")


def A():
    print("A-Start")
    B()
    print("A-End")


A()


def X():
    print("X1")
    print("X2")
    Y()
    print("X3")


def Y():
    print("Y1")
    print("Y2")
    print("Y3")

X()