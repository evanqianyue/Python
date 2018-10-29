# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/28 20:05
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

listNum = [2, 3, 1, 5, 6, 9, 9, 9, 8]
listNum.sort()

maxNum = listNum[len(listNum)-1]
maxNumCount = listNum.count(maxNum)
print(maxNumCount)
print(listNum[len(listNum)-maxNumCount-1])
