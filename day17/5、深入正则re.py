# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/2 12:21
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import re

str1 = "sunck    is good"
str2 = "sunck#####is good"
print(re.split(r" +", str1))
print(re.split(r"#+", str2))

str3 = "sunck is good,sunck is good,sunck is good,sunck is good"
b = re.findall(r"sunck.*?good", str3)

print(b)
for i in b:
    print(i)

"""
字符串替换和修改
re.sub(pattern, repl, string, count=0)
re.subn(pattern, repl, string, count=0)

参数：

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

区别：

sub     返回字符串
subn    返回元组，第一个元素是修改后的字符串，第二个元素是被替换的次数

"""
str4 = "sunck is good,sunck is good,sunck is good,sunck is good"
print(re.sub(r"(good)", "nice", str4, count=1))  # 返回的是str

print(re.subn(r"(good)", "nice", str4, count=6))  # 返回的是tuple

"""
分组：
概念：除了简单的判断是够匹配之外，正则表达式还有提取子串的功能。
用()表示的就是提取出来的分组

"""

str5 = "010-53265448"
m = re.match(r"(\d{3})-(\d{8})", str5)
# 使用序号获取对应的信息
# group(0) 表示原始字符串
print(m.group(0), m.group(1), m.group(2))
# 结果 010-53265448 010 53265448

m = re.match(r"(?P<first>\d{3})-(?P<second>\d{8})", str5)
print(m.group("first"), m.group("second"))

"""
compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：

re.compile(pattern[, flags])

参数：

pattern : 一个字符串形式的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和' # '后面的注释

"""

# re.compile 编译正则对象
pat = r"^1(([3578]\d)|(47))\d{8}$"
re_telephone = re.compile(pat)

print(re_telephone.match("13758312556"))



