# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 17:31
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from multiprocessing import Pool
import time
import os


def run(id):
    print("子进程开始——%d——%s" % (id, os.getpid()))
    time.sleep(1)
    print("子进程结束——%d——%s" % (id, os.getpid()))


if __name__ == "__main__":

    print("父进程开始")

    # 创建多个进程
    # 进程池
    # 同时执行的进程数量,默认CPU核心数

    pp = Pool()
    for i in range(1, 11):
        # 创建进程，放入进程池统一管理
        pp.apply_async(run, args=(i,))

    # 调用join之前必须先调用close，并且调用close就不能再继续添加新的进程了
    pp.close()
    pp.join()

    # 全局变量在多个进程中不能共享
    print("父进程结束")
