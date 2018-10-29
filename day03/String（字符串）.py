# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/27 21:16
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

# 创建字符串
str1 = "Tom is very good"
str3 = "Tom is very nice"
str5 = "Tom is very handsome"

# 字符串连接
str6 = "Tom is "
str7 = "very good"
str8 = str6 + str7
print(str8)

# 输出重复字符串
str9 = "good "
str10 = str9 * 3
print(str10)

# 访问字符串中某个字符
# 通过索引下标查找字符，索引从0开始
str11 = "Tom is handsome"
print(str11[1])
# str11[0] = 'a'  # 报错，字符串不可变

# 截取字符串的一部分
print(str11[2:4])

# 从头截取到下标之前
print(str11[:5])

# 从给定下标处开始截取到结尾
print(str11[16:])

# 倒序
print(str11[::-1])

str18 = "Tom is a good man"
print("good" in str18)
print("good" not in str18)

# 格式化输出
num = 10
s19= "hello"
f = 10.1267
print("num =", num)  # 自带一个空格
# %d %s %f占位符 %.3f 精确到3位小数（会四舍五入）
print("num = %d, s19 = %s, f = %.3f" % (num, s19, f))
# 如果字符串内有很多换行，\n写在一行不好阅读
print("num = %d\ns19 = %s\nf = %.3f" % (num, s19, f))


print("\\n")

# 制表符
print("tom\tgood")

# python 允许用r表示内部的字符串默认不转义
print(r"C:\Users\Evan\n\t\day02")
print("C:\\Users\\Evan\\n\\t\\day02")   # windows \
print("C:/Users/Evan/n/t/day02")    # linux /


# eval(str)
# 功能：将字符串str当成有效的表达式来求值，并返回计算结果
num1 = eval("123")
print(num1)
print(eval("12-3"))
print(eval("-123"))

# len(str)
# 返回字符串长度

# str.lower()
# 字母转换为小写
str20 = "ApPle"
print(str20.lower())
print(str20)

# str.upper()
# 字母转换为大写
str21 = "hellO"
print(str21.upper())
print(str21)

# swapcase()
# 大写换小写，小写换大写
str22 = "tom is a GOOD man"
print(str22.swapcase())  # TOM IS A good MAN

# capitalize
# 首字母大写
print(str22.capitalize())   # Tom is a good man

# title
# 每个单词首字母大写
print(str22.title())  # Tom Is A Good Man


# center(width, fillchar)
str25 = "Tom is a nice man"
print(str25.center(30, "%"))  # ******Tom is a nice man*******

# rjust 和 ljust
print(str25.rjust(30, "%"))
print(str25.ljust(30, "%"))

# zfill（）
print(str25.zfill(30))

# string.count(str, beg=0, end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print(str25.count("nice", 10, len(str25)))

# string.find(str, beg=0, end=len(string))
# 从左往右检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1 （得到的是第一次出现的）
print(str25.find("nice", 2, 13))

# rfind 类似于 find()函数，不过是从右边开始查找.
print(str25.rfind("nice", 2, 13))


print("_______")
# string.index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在 string中会报一个异常.
str26 = "Tom is a nice man"
# print(str26.index("nice", 2, 5))  # ValueError: substring not found

# string.rindex( str, beg=0,end=len(string)) 类似于 index()，不过是从右边开始.
print(str26.rindex("is", 2, 13))


# lstrip() 截掉 string 左边的空格
str27 = "  Toms is a nice man"
print(str27.lstrip())

str28 = "***Evan is a nice man"
print(str28.lstrip("*"))

# rstrip() 截掉 string 右边的空格
str29 = "Jack is a nice man     "
print(str29.lstrip())

# strip() 截掉 string 两边的空格(默认)
str30 = "******Emma is a nice man*****"
print(str30.strip("*"))

# ord()
"""
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
"""
print(ord("a"))


# join() 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
str88 = "-"
seq = ["a", "b", "c"]  # 字符串序列
print(str88.join(seq))


# string.split(str="", num=string.count(str))
# 以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
# 参数
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。
str88 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str88.split())
print(str88.split(' ', 1))

# split(str="", num)
# 以str为分隔符截取字符串，指定num，则仅截取num个字符串
str38 = "sunk**is*a*****good***man"
str39 = "sunk,is,a,good,man"

print(str38.split("*"))
print(str38.split("*", 2))  # 被分成num+1个
print(str39.split(","))
# splitlines() # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

str88 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str88.splitlines())
print(str88.splitlines(True))


# replace(oldstr, newstr, count)
# 用newstr替换oldstr,默认是全部替换，如果指定了count，那么只替换前count个
str44 = "Tom is a good good man "
str45 = str44.replace("good", "nice", 1)
print(str44)
print(str45)

# maketrans() 不可控，较少用
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# a-6   c-5
t46 = str.maketrans("ac", "65")
str47 = "sunck is a good man"
str48 = str47.translate(t46)
print(str48)

# starswith(obj,beg=0,end=len(str))
# 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
str49 = "sunck is a good man"
print(str49.startswith("sunck", 5, 10))

# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
str50 = "sunck is a good man"
print(str49.endswith("good", 10, 15))  # True
print(str49.endswith("good", 10, 16))  # False

# 编码
# encode(encoding="utf-8", errors="strict")
# encode() 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
str51 = "he is good好的凯"
data52 = str51.encode("utf-8")
print(data52)
print(type(data52))

# 解码  注意：要与编码时的编码格式一致
# decode(encoding='UTF-8',errors='strict'))
# decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
str53 = data52.decode("gbk", "ignore")  # 可能会有乱码
print(str53)

# isalpha() 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
str54 = 'a'
str55 = 'a1'

print(str54.isalpha())  # True
print(str55.isalpha())  # False

# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
str56 = "la123"
str57 = "la12 3"
print(str56.isalnum())
print(str57.isalnum())

# isupper()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
str58 = "LA123"
str59 = "la123"
print(str58.isupper())
print(str59.isupper())

# islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
str58 = "LA123"
str59 = "la123"
print(str58.isupper())
print(str59.isupper())

# istitle() 如果字符串是标题化的(见 title())则返回 True，否则返回 False
str58 = "Tom Is"
str59 = "Tom is"
print(str58.istitle())
print(str59.istitle())

# isdigit()
# 如果字符串中只包含数字字符返回true
print("123".isdigit())
print("123a".isdigit())

# isnumeric 同上
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
print("123".isnumeric())
print("123a".isnumeric())

# isdecimal
# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
print("123".isdecimal())
print("123a".isdecimal())

# space
# 如果字符串中只包含空白，则返回 True，否则返回 False.
print("^^^")
print(" ".isspace())  # True
print("\n".isspace())  # True
print("\t".isspace())  # True
print("\r".isspace())  # True
print("\f".isspace())  # True
print("123a".isspace())  # False
