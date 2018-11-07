# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 11:59
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import os
import time

# 获取操作系统类型 nt->windows ,posix->linux,unix,mac os x
print(os.name)

# 打印操作系统详细信息（windows不适用）
# print(os.uname())
# 所有环境变量
print(os.environ)
# 获取某个环境变量
print("path:*****", os.environ.get('path'))

# 获取当前工作目录
print(os.curdir)

# 获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())

# os.listdir(path)
print(os.listdir(os.getcwd()))
# 返回path指定的文件夹包含的文件或文件夹的名字的列表。

# os.mkdir() 在当前目录下创建新目录
# os.rmdir()
os.mkdir("123")
os.rmdir("123")

# os.stat(file) 获取文件属性
print(os.stat("./os模块.py"))

# os.rename(src, dst)  重命名文件或目录，从 src 到 dst
# os.rename("234", "test")
# time.sleep(1)
# os.rename("test", "234")

# os.remove(file) 删除普通文件
# try:
#     os.remove("test.txt")
# finally:
#     print("ok!")

# os.system(command)
# os.system("notepad")
os.system("taskkill /f /im notepad.exe")

# 有些方法存在os模块里，还有些存在于os.path
# os.path.abspath 查看绝对路径
print(os.path.abspath("./"))
print(os.path.basename(os.path.abspath(os.getcwd())))
print(os.path.dirname(os.path.abspath(os.getcwd())))

# os.path.join(path1[, path2[, ...]])拼接
# path2,path3...不能有斜杠
print(os.path.join('root', 'test', 'runoob.txt'))  # 将目录和文件名合成一个路径

# split 把路径分割成 dirname 和 basename，返回一个元组
print(os.path.split(os.getcwd()))

# 获取拓展名
p2 = r"C:\Users\QianYue\IdeaProjects\Python\day08"
p3 = r"C:\Users\QianYue\IdeaProjects\Python\day08\os模块.py"
p4 = r"C:\Users\QianYue\IdeaProjects\Python\day08\os模块2.py"
print(os.path.splitext(os.getcwd()))  # ('C:\\Users\\QianYue\\IdeaProjects\\Python\\day08', '')
print(os.path.splitext(p3))  # ('C:\\Users\\QianYue\\IdeaProjects\\Python\\day08\\os模块', '.py')

# os.path.isdir 判断是够是目录
print(os.path.isdir(p2))  # True
print(os.path.isdir(p3))  # False

# os.path.isfile 判断文件是否存在
print(os.path.isfile(p3))  # True
print(os.path.isfile(p2))  # False

# os.path.exists 判断目录是否存在
print(os.path.exists(p2))  # True
print(os.path.exists(p4))  # False

# os.path.getsize 获得文件大小（字节）
print(os.path.getsize(p3))  # True



