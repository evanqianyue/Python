# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 22:55
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import threading
import os


def run(id):
    print("子线程开始%s" % threading.current_thread().name)
    print("id:%d" % id)
    print("子线程结束%s" % threading.current_thread().name)


if __name__ == "__main__":
    # 任何进程默认就会启动一个线程，称为主线程，主线程可以启动新的子线程
    print("启动主线程%s" % threading.current_thread().name)

    # 创建子线程,name 子线程名称
    t = threading.Thread(target=run, name="rootThread", args=(2,))

    t.start()
    t.join()

    print("结束主线程%s" % threading.current_thread().name)
