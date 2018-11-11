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

sql = "select * from bandcard where money >= 500;"

# fetchone()
# 功能：获取下一个查询结果集，结果集是一个对象

# fetchall()
# 功能：接收全部的返回的行

# rowcount
# 是一个只读属性，返回execute()

try:
    cursor.execute(sql)
    data = cursor.fetchall()
    # data = cursor.rowcount
    for row in data:
        print("%d--%d" % (row[0], row[1]))

except BaseException as e:

    print("Exception:", e)

cursor.close()
db.close()
