# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/30 14:27
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import collections

queue = collections.deque()


queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
