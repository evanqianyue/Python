# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 17:19
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from multiprocessing import Process
from time import sleep


num = 100

def run():
    print("子进程开始")
    global num
    num += 1

    print("子进程结束")


if __name__ == "__main__":
    print("父进程开始")

    p = Process(target=run)
    p.start()
    p.join()

    # 全局变量在多个进程中不能共享
    print("父进程结束,num:%d" % num)
