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


def run():
    print("子进程启动")

    time.sleep(1.0)

    print("子进程结束")


if __name__ == "__main__":
    print("主（父）进程启动 %d" % os.getpid())

    # 创建子进程
    # target说明执行的任务
    p = Process(target=run)

    # 启动进程
    p.start()

    # 父进程的结束不影响子进程
    # p.join() 让父进程等待子进程结束再执行父进程

    p.join()

    print("父进程结束")
