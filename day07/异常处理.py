# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 22:00
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
try:
    语句t
except 错误码 as e：
    语句1
except 错误码 as e：
    语句2
    ……
except 错误码 as e：
    语句n
else：   
    语句e

注意：这个else可有可无

作用：用来检测try语句块中的错误，从而让except语句捕获错误信息并处理

逻辑：当程序执行到try-except-else语句时
1、如果当try“语句t”执行出现错误，会匹配第一个错误码，如果匹配上就执行对应语句
2、如果当try“语句t”执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，或者到程序的最上层。
3、如果当try“语句t”执行没有错误，执行else下的语句语句e（前提提交是有else：语句e）
4、finally:语句f都会执行
"""
try:
    print(3 / 0)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Demo is ok!")

# 使用except带着多种异常
try:
    print(3 / 0)
except (NameError, ZeroDivisionError):
    print("出现NameError或者ZeroDivisionError")

# 错误其实是class(类)，所有错误都继承于BaseException
try:
    print(3 / 0)
except BaseException as e:
    print(e)

try:
    print(3 / 0)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
finally:
    print("This is Finally!")
