# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 16:46
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
函数的本质：对功能的封装

优点：
1、简化代码结构，增加代码复用度
2、如果想修改某些功能或者调试某个bug，只需要修改对应的函数即可
"""


# 无返回值
def myprint():
    print("Hello word!")


if __name__ == '__main__':
    myprint()
