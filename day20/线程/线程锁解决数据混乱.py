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

lock = threading.Lock()


def run(id):
    print("子进程开始")
    global num

    for i in range(1000000):
        # 锁
        # 确保了这段代码只能由一个线程从头到尾完整的执行
        # 阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以效率降低了
        # 由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能造成死锁，导致多个线程挂起，只能靠操作系统强制终止
        '''
        
        Lock.acquire()
        try:
            num += id
            num -= id

        # 释放锁
        finally:
            Lock.release()
        '''

        # 与上面代码功能相同，with lock 自动上锁与解锁
        with lock:
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
