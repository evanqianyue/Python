# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/10 18:13
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import redis


class myRedis():
    def __init__(self, host="localhost", port=6379, passwd=None):
        self.__redis = redis.StrictRedis(host=host, port=port, password=passwd)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""


redis1 = myRedis()
redis1.set("p4", "p4")
print(redis1.get("p1"))
