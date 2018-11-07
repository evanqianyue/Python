# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 19:04
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import threading
import time,os


# 线程条件变量
cond = threading.Condition()


def run1():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i, os.getpid())
            # time.sleep(1)
            cond.wait()
            cond.notify()


def run2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i, os.getpid())
            # time.sleep(1)
            cond.notify()
            cond.wait()


threading.Thread(target=run1, name="run1").start()
threading.Thread(target=run2, name="run2").start()
