# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 14:02
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
递归调用：一个函数，调用的是自身，成为递归调用
递归函数：一个会调用自身的函数称为递归函数

凡是循环能干的事，递归都能干

方式：
1、找出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，求出本次的结果
"""


# 求1+2+3+……+n

# mySum(4)+5=mySun(5)
# mySum(3)+4=mySun(4)
# mySum(2)+3=mySun(3)
# mySum(1)+2=mySun(2)
# mySum(0)+1=mySun(1)

def mySum(n):
    if n == 1:
        return n
    else:
        return n + mySum(n - 1)


print(mySum(5))

# 5+mySum(4)
# 5+4+mySum(3)
# ……
# 5+4+3+2+1
