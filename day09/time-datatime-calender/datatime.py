# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 23:03
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
"""
datetime    同时有时间和日期
timedelta   主要用于计算时间的跨度
tzinfo      时区相关
time        只关注时间
data        只关注日期

"""
import datetime

print(dir(datetime))

# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))  # <class 'datetime.datetime'>

# 获取指定时间
d2 = datetime.datetime(1999, 10, 1, 10, 28, 25, 123456)
print(d2)


# 将时间转为字符串
d3 = d1.strftime("%Y-%m-%d %H:%M:%S")
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

# 将格式化字符串转为datetime对象
# 注意：转换的格式要与字符串一致
d4 = datetime.datetime.strptime(d3, "%Y-%m-%d %X")
print(d4)

d5 = datetime.datetime(1999, 10, 1, 7, 40, 25, 123456)
d6 = datetime.datetime.now()
d7 = d6-d5
print(type(d7))
# 间隔的天数
print(d7.days)
# 间隔天数除外的秒数
print(d7.seconds)


