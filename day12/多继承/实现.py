# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/31 16:15
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from child import Child


def main():
    c = Child(30, 300)
    print(c.money, c.faceValue)

    # 注意：父类中方法相同，默认调用的是括号内排前面的
    c.func()


if __name__ == "__main__":
    main()
