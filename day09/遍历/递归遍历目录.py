# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 14:44
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import os

path = r"C:\Users\QianYue\IdeaProjects\Python"


def getAllDirRe(path, sp=""):
    filesList = os.listdir(path)
    # print(filesList)
    sp += "   "
    # 组成路径
    for fileName in filesList:
        # 判断是否是路径（用绝对路径）
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录：%s" % fileName)
            getAllDirRe(fileAbsPath, sp)
        else:
            print(sp + "普通文件：%s" % fileName)


getAllDirRe(path)
