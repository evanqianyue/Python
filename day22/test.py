# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/10 15:35
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
from evansql import mySql

testsql = mySql("192.168.1.2", "root", "admin", "course")
data = testsql.delete("delete from bandcard where id = 2;")
print(data)