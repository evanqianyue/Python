# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 19:19
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import os


def getAllDirDe(path):
    stack = []
    stack.append(path)
    print(stack)
    # 处理栈
    while len(stack) != 0:
        # 从堆栈里取出数据
        dirpath = stack.pop()
        filesList = os.listdir(dirpath)
        print(filesList)
        for fileName in filesList:

            print("filelist:", filesList)
            # 处理每一个文件，如果是普通文件则打印出来，如果是目录则将该目录的地址压入栈
            fileAbsPath = os.path.join(dirpath, fileName)
            if os.path.isdir(fileAbsPath):
                # 如果是目录则压栈
                print("目录：", fileName)
                stack.append(fileAbsPath)
            else:
                # 不是目录则打印
                print("普通文件：", fileName)


getAllDirDe(r"D:\file")
