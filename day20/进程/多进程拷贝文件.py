# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 21:51
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from multiprocessing import Pool
import os
import time

path = r"C:\Users\QianYue\IdeaProjects\Python\day20\file"

toPath = r"C:\Users\QianYue\IdeaProjects\Python\day20\copy_file"


def copyFiles(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


if __name__ == "__main__":
    start = time.time()
    pp = Pool()
    fileList = os.listdir(path)
    for fileName in fileList:
        pp.apply_async(copyFiles(os.path.join(path, fileName), os.path.join(toPath, fileName)))

    pp.close()
    pp.join()
    end = time.time()
    print("%.2f" % (end - start))
