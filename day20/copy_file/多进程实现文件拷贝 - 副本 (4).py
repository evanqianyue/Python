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

if __name__ == "__main__":
    fileList = os.listdir(path)
