# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 9:38
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
1、 打开文件
2、 读取内容
3、 关闭
"""

"""
1、打开文件
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
参数说明:

file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型



r: 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
rb:以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等
r+:打开一个文件用于读写。文件指针将会放在文件的开头。

w:打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb:以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+:打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

a:打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+:	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
"""

# 读取所有内容
with open(r"D:\file\read.txt", "r+") as f:
    print(f.read())

# 读取指定字符数
with open(r"D:\file\read.txt", "r+") as f:
    print(f.read(2))
    print(f.read(5))  # 从刚才的位置继续往后

# 读取整行，包括 "\n" 字符串
with open(r"D:\file\read.txt", "r+") as f:
    print("readline1:", f.readline())  # 第一行
    print("readline2:", f.readline())  # 第二行

# 读取指定字符数
with open(r"D:\file\read.txt", "r+") as f:
    print("readlineX:", f.readline(6))  # 读取第一行的某些字符串，然后跳到下一行
    print(f.read())

# seek() 方法用于移动文件读取指针到指定位置。
"""
fileObject.seek(offset[, whence])
参数
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数

whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
0 代表从文件开头开始算起，
1 代表从当前位置开始算起，
2 代表从文件末尾算起。
"""

with open(r"D:\file\read.txt", "r+") as f:
    print(f.read(2))
    print(f.seek(0))
    print(f.read(2))

# 写入加换行
with open(r"D:\file\write.txt", "a+") as f:
    f.write("hello!\n")  # 将信息写入缓冲区
    f.flush()  # 刷新缓冲区，立刻写入文件，而不是被动等待，自动刷新缓冲区写入

# 编码
with open(r"D:\file\write.txt", "wb") as f:
    str2 = "Hello World!凯\n"
    f.write(str2.encode("utf-8"))

with open(r"D:\file\write.txt", "rb") as f:
    print(f.read().decode("utf-8"))

# 不报错
with open(r"D:\file\write.txt", "r", encoding="gbk", errors="ignore") as f:
    print(f.read())

# 报错
with open(r"D:\file\write.txt", "r", encoding="gbk") as f:
    print(f.read())
