# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/10 18:08
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import redis

# 连接
r = redis.StrictRedis(host="localhost", port=6379)

# set
r.set("hello", "helloword")

# get
print(r.get("hello"))

# pipline
# 缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("p1", "p1")
pipe.set("p2", "p2")
pipe.set("p3", "p3")
pipe.execute()
