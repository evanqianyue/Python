# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/10 12:49
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import pymysql
import time

# 数据库地址
# 用户名
# 密码
# 要链接的数据库名

db = pymysql.connect("192.168.1.2", "root", "admin", "course")

# 创建一个cursor对象
cursor = db.cursor()


sql = "insert into bandcard values('1','1000'),('2','333'),('3','500'),('4','500');"

try:
    cursor.execute(sql)
    db.commit()

except BaseException as e:
    db.rollback()
    print("Exception:", e)

cursor.close()
db.close()
