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

# 创建一个全局的ThreadingLocal对象
# 每个线程有独立的存储空间
# 每个线程对ThreadLocal对象都可以读写，但是互不影响

local = threading.local()


def run(x, n):
    # print("子进程开始")
    x += n
    x -= n
    # print("子进程结束")


def func(n):
    local.x = num
    for i in range(1000000):
        run(local.x, n)
        # local.x += n
        # local.x -= n
    print("%s-%d" % (threading.current_thread().name, local.x))


if __name__ == "__main__":
    print("父进程开始")

    t1 = threading.Thread(target=func, args=(1,), name="线程t1")
    t2 = threading.Thread(target=func, args=(3,), name="线程t2")

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("父进程结束,num:%d" % num)

    # 作用：为每个线程绑定一个数据库，HTTP请求，用户身份信息等
    # 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
