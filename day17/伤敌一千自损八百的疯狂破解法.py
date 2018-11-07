# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/1 20:38
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import itertools
import time

password = ("".join(x) for x in itertools.product("0123456789", repeat=3))

while True:
    try:
        time.sleep(0.5)
        str2 = next(password)
        print(str2)
    except BaseException as e:
        print(e)
