# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 12:41
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import threading
import time

def func():
    event = threading.Event()

    def run():
        for i in range(5):
            # 阻塞，等待事件
            event.wait()
            # 重置
            event.clear()
            print("%d" % i)
    t = threading.Thread(target=run).start()
    return event


if __name__ == "__main__":

    e = func()
    # 触发事件（可以在任何地方触发）
    for i in range(5):
        e.set()
        time.sleep(2)
    # print("父进程结束")
