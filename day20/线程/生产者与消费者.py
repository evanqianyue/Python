# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/7 13:16
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import threading, queue
import time, random


# 生产者
def product(id, q):
    while True:
        num = random.randint(0, 1000)
        q.put(num)
        print("生产者%d生产了%d" % (id, num))
        time.sleep(3)
    q.task_done()


# 消费者
def customer(id, q):
    while True:
        item = q.get()
        if item is None:
            break

        print("消费者%d消费了%d" % (id, item))
        time.sleep(2)


if __name__ == '__main__':

    q = queue.Queue()
    # 启动生产者
    for i in range(4):
        threading.Thread(target=product, args=(i, q)).start()
    # 启动消费者
    for i in range(3):
        threading.Thread(target=customer, args=(i, q)).start()
