# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 16:55
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


# 形参（形式参数）：定义函数时小括号中的变量，本质是变量
# 参数必须按照顺序传递
# 默认参数放到最后
def myPrint(string, age, hobby=None):
    print(string, age, hobby)
    return None


# 实参（实际参数）：调用函数时给函数传递的数据，本质是值
myPrint("aaa", 20)
myPrint("aaa", 20, "test")

print(myPrint("aaa", 20))
