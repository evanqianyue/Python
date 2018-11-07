# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 20:49
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import os
import collections


def getAllDirQu(path):
    queue = collections.deque()
    queue.append(path)
    # print(queue)
    while len(queue) != 0:
        dirpath = queue.popleft()
        filesList = os.listdir(dirpath)
        for fileName in filesList:

            print("filelist:", filesList)
            # 处理每一个文件，如果是普通文件则打印出来，如果是目录则将该目录的地址加入队列
            fileAbsPath = os.path.join(dirpath, fileName)
            if os.path.isdir(fileAbsPath):
                # 如果是目录则加入队列
                print("目录：", fileName)
                queue.append(fileAbsPath)
            else:
                # 不是目录则打印
                print("普通文件：", fileName)

getAllDirQu(r"D:\file")