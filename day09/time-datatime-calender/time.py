# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 22:00
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
UTC(世界协调时间)：格林尼治天文时间，世界标准时间，中国：UTC+8
DST(下令时):是一种节约能源而人为规定的时间制度，在夏季调快1小时
"""

"""
时间的表示形式：
1、时间戳
以整型或者浮点型表示时间的一个以秒为单位的时间间隔。基础值是1970年1月1日零点开始
2、元组
9个整型内容
year
month
day
hours
minutes
seconds
weekday
Julia day
flag(1 或 -1 或 0)
3、格式化字符串
2018-10-30 22:11:08
    Commonly used format codes:
    
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
    %x  本地日期格式 (mm/dd/yy)
　　 %X  本地时间格式 (%H:%M:%S)

"""
import time

# 得到时间戳
c = time.time()
print(c)

# 将时间转换成格林尼治时间元组
t = time.gmtime(c)
print(t)

# 将时间转换成本地时间元组
b = time.localtime(c)
print(b)

# 将本地时间转成时间戳
m = time.mktime(b)
print(m)  # 与C不一致，精度问题

# 将时间元组转成字符串
s = time.asctime(b)
print(s)

# 将时间戳转为字符串
p = time.ctime(c)
print(p)

# 格式化输出,参数2位时间元组，如果没有参数2，默认转当前时间
str1 = time.strftime("%Y-%m-%d %H:%M:%S")
str2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

print("str1:", str1)
print("str2:", str2)

# 将时间字符串转成时间元组
w = time.strptime(str1, "%Y-%m-%d %H:%M:%S")
print(w)

# 延迟，整型或者浮点
# time.sleep(4.5)

# 返回当前程序的cpu执行时间
# Unix系统始终返回全部的运行时间
# windows从第二次开始，都是以第一次调用此函数的开始时间粗作为基数
y1 = time.clock()
print(y1)

time.sleep(1)

y2 = time.clock()
print(y2)
