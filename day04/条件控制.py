# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/28 21:30
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

age = int(input("请输入年龄："))
if age < 0:
    print("Error!")
elif age < 10:
    print("少年!")
elif age < 18:
    print("青年!")
else:
    print("成人!")

