# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 8:58
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
2个线程同时工作，一个存，一个取
可能导致数据异常
"""

import threading
from time import sleep

num = 100

bar = threading.Barrier(3)


def run():
    print("start %s" % (threading.current_thread().name))
    sleep(3)
    bar.wait()
    print("end %s" % (threading.current_thread().name))


if __name__ == "__main__":
    print("父进程开始")

    for i in range(6):
        t1 = threading.Thread(target=run).start()

    print("父进程结束,num:%d" % num)

    # 作用：为每个线程绑定一个数据库，HTTP请求，用户身份信息等
    # 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
