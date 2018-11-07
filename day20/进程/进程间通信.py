# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 22:23
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from multiprocessing import Process, Queue
import time
import os


def read(q):
    print("启动读子进程%s" % os.getpid())
    while True:
        value = q.get(True)
        print("value=" + value)

    print("结束读子进程%s" % os.getpid())


def write(q):
    print("启动写子进程%s" % os.getpid())
    for chr in ["A", "B", "C", "D"]:
        q.put(chr)
        time.sleep(1)
    print("结束写子进程%s" % os.getpid())


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()

    # pr进程里是个死循环，无法等待其结束，只能强行结束
    pr.terminate()

    print("父进程结束")
