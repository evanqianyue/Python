# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 7:45
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import calendar

# 某年某月
print(calendar.month(2019, 10))

# 返回指定年的日历
print(calendar.calendar(2018))

# 判断是否闰年
print(calendar.isleap(2010))
print(calendar.isleap(2000))

# 返回某个月的weekday的第一天和这个月的所有天数
print(calendar.monthrange(2017, 7))

# 返回某个月以每周为元素的列表，list形式展示
print(calendar.monthcalendar(2017, 7))

