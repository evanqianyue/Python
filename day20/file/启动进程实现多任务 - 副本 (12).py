# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 16:18
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
multiprocessing 库
跨平台版本的多进程模块，提供一个process类来代表一个进程对象
"""
from multiprocessing import Process
import time
import os


def run1(str1, str2):
    while True:
        # os.getpid 获取当前进程ID
        # os.getppid 获取当前进程的父进程ID
        print("he is %s %s————%d————%d" % (str1, str2, os.getpid(), os.getppid()))
        time.sleep(1.0)

def run2(str1):
    while True:
        # os.getpid 获取当前进程ID
        # os.getppid 获取当前进程的父进程ID
        print("he is %s" % (str1))
        time.sleep(1.0)


if __name__ == "__main__":
    print("主（父）进程启动 %d" % os.getpid())

    # 创建子进程
    # target说明执行的任务
    p = Process(target=run1, args=("nice","man"))

    # 启动进程
    p.start()

    while True:
        print("she")
        time.sleep(1.0)
