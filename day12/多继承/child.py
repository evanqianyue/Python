# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 16:04
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from father import Father
from mother import Mother


class Child(Mother, Father):
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)



def main():
    pass


if __name__ == "__main__":
    main()