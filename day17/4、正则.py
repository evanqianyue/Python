# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/1 20:44
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import re

# re.match(pattern, string, flags=0)
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

"""
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

"""
# re.match 扫描整个字符串并返回第一个成功的匹配。
print(re.match("www", "www.baidu.com"))
print(re.match("www", "www.baidu.com").span())
# print(re.match("www", "www.baidu.com").match())  # match 不能用
# 会报错 AttributeError: '_sre.SRE_Match' object has no attribute 'match'
print(re.match("www", "ww.baidu.com"))
print(re.match("www", "baidu.www.com"))
print(re.match("www", "wwW.baidu.com"))
print(re.match("www", "wwW.baidu.com", flags=re.I))

# re.search 扫描整个字符串并返回第一个成功的匹配。
print("*******************************\n")

print(re.search("www", "www.baidu.com"))
print(re.search("www", "www.baidu.com").span())
# print(re.search("www", "www.baidu.com").search())
print(re.search("www", "ww.baidu.com"))
print(re.search("www", "baidu.www.com"))
print(re.search("www", "wwW.baidu.com"))
print(re.search("www", "wwW.baidu.com", flags=re.I))

# re.findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。

print("*******************************\n")

print(re.findall("www", "wwW.www.baidu.com", flags=re.I))

print("*****单个字符与数字*****")

"""
.               匹配除换行符以外的任意字符
[0123456789]    字符集合，表示匹配方括号内所包含的任意一个字符
[sunck]         "s" "u" "n" "c" "k" 中任意一个字符
[a-z]           匹配任意小写
[A-Z]           匹配任意大写
[0-9]           匹配任意数字，类似[0123456789]
[0-9a-zA-Z]     匹配任意数字或字母
[0-9a-zA-Z_]    匹配任意数字或字母或下划线
[^sunck]        匹配除了sunck这几个字母以外的所有字符，中括号里的成为^脱字符，表示不匹配集合中的字符
[^0-9]          匹配所有非数字字符
\d              匹配数字，效果同[0-9]
\D              匹配非数字字符，效果同[^0-9]
\w              匹配任意数字或字母或下划线，效果同[0-9a-zA-Z_]
\W              匹配非数字、字母、下划线，效果同[^0-9a-zA-Z_]
\s              匹配任意的空白符（空格，换行，回车，换页，制表）效果同[ \f\n\r\t] 
\S              匹配任意的非空白符，效果同[^ \f\n\r\t]
"""

print(re.search(".", "sunck is a good man 6"))
print(re.findall("\w", "sunck is a good_man 6"))

print("*****锚字符（边界字符）*****")
"""
^       行首匹配，与[]内不是一个意思
$       行尾匹配
\A      匹配字符串开始，与^的区别是：\A只匹配整个字符串的开头，即使在re.M模式下页不会匹配它行的行首
\Z      匹配字符串开始，与^的区别是：\Z只匹配整个字符串的行尾，即使在re.M模式下页不会匹配它行的行尾
\b      匹配一个单词的边界，也就是指单词和空格间的位置
\B      匹配非单词边界
"""

print(re.findall("^sunck", "sunck is a good man \nsunck is a good man", flags=re.M))  # 2个
print(re.findall("sunck$", "sunck is a good man \nsunck is a good man", flags=re.M))  # 0个

print(re.findall("\Asunck", "sunck is a good man \nsunck is a good man", flags=re.M))  # 1个
print(re.findall("\Zsunck", "sunck is a good man \nsunck is a good man", flags=re.M))  # 0个
print(re.findall(r"er\b", "never ", flags=re.M))  # 1个
print(re.findall(r"er\b", "nevera", flags=re.M))  # 0个
print(re.findall(r"er\B", "never ", flags=re.M))  # 0个
print(re.findall(r"er\B", "nevera", flags=re.M))  # 1个

print("*****匹配多个字符*****")
"""
说明：下方的xyz均为假设的普通字符，不时正则表达式的元字符（xyz）
匹配小括号内的xyz（作为一个整体去匹配）
*	匹配0个或多个的表达式。
+	匹配1个或多个的表达式。
?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式

"""

print(re.findall(r"sunck", "sunck is a good man,sunck is a good man"))

# 需求：提取sunck...man

print("*****提取sunck...man*****")
str = r"sunckman!sunck is a nice man！sunck is a very nice man!"
print(re.findall(r"sunck.*man", str))
# 上面的结果['sunck is good man!sunck is a nice man！sunck is a very nice man']

print(re.findall(r"sunck.+man", str))
# 上面的结果['sunck is good man!sunck is a nice man！sunck is a very nice man']

print(re.findall(r"sunck.*?man", str))
print(re.findall(r"sunck.+?man", str))

# 上面的结果['sunck is good man', 'sunck is a nice man', 'sunck is a very nice man']
