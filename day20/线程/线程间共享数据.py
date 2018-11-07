# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 23:06
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
多线程和多进程最大的不同在于，多进程，同一个变量，各自有一份拷贝在每个进程中。而在多线程中，所有变量都有所有线程共享
"""

import threading
from time import sleep

num = 100


def run(id):
    print("子进程开始")
    global num
    for i in range(1000000):

        num += id
        num -= id

    print("子进程结束")


if __name__ == "__main__":
    print("父进程开始")

    t1 = threading.Thread(target=run, args=(1,))
    t2 = threading.Thread(target=run, args=(3,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 全局变量在多个进程中不能共享
    print("父进程结束,num:%d" % num)
