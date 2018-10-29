# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 16:15
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
set：类似dict，是一组key的集合
本质：无序和无重复元素的集合
"""

# 创建
# 需要一个list或者tuple或者dict作为输入集合
# 重复元素会被自动过滤
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 3, 4, 5, 1])
print(s1, s2)

s3 = set((1, 2, 3, 3, 2, 1))
print(s3)

# 只有键
s4 = set({"tom": 80, "evan": 90})
print(s4)

# 添加
s5 = set([1, 2, 3, 4, 5])
s5.add(6)
s5.add(6)  # 重复添加无效果
s5.add((7, 8, 9))
# s5.add([7, 8, 9])  # set的元素不能是list，列表可变,TypeError: unhashable type: 'list'
# s5.add({1:"a"})  # set的元素不能是dict,字典的值可变TypeError: unhashable type: 'list'
print(s5)


# 插入整个list、tuple、str
print("********")
s6 = set([1, 2, 3, 4, 5])
s6.update([7, 8, 9])  # set的元素不能是list，列表可变,TypeError: unhashable type: 'list'
# s5.add({1:"a"})  # set的元素不能是dict,字典的值可变TypeError: unhashable type: 'list'
print(s6)

