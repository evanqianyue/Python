# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 8:49
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

myList = [45, 32, 8, 33, 12, 22, 19, 97]
# myList = [1, 2, 3, 4, 6, 5]
length = len(myList)

for i in range(0, length - 1):  # 这个循环负责设置冒泡排序进行的次数
    flag = 0

    for j in range(0, length - 1 - i):  # j为列表下标
        if myList[j] > myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]
            flag += 1
        print(myList, flag)
    if 0 == flag:
        break
    print("Another Loop!")

print("final:", myList)

