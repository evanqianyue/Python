# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/28 8:22
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

list2 = [1, 2, 3]
print(list2)

# 列表的重复
list3 = list2 * 3
print(list3)

# 判断元素是否在列表中
print(3 in list2)

# 列表截取
list3 = [1, 2, 3, 4, 5]
print(list3[::-1])

# 二维列表
list4 = [[1, 2], [2, 3], [3, 4]]
print(list4[1])

# 列表方法
# append 在末尾添加新的元素
list5 = ["a", 1]
list5.append(2)
list5.append([1, 2])
print(list5)

# extend 在末尾追加另一个列表中的多个值
list5.extend([3, 3])
print(list5)

# insert() 函数用于将指定对象插入列表的指定位置。
list6 = [2, 3, 4]
list6.insert(0, 30)
print(list6)

# pop() 默认移除最后一个元素
list6.pop(1)
print(list6)

# remove 移除列表中的某一个元素第一个匹配结果
list7 = [1, 2, 3, 4, 4, 5, 6]
list7.remove(4)
print(list7)

# clear 全部清除
list7.clear()
print(list7)


# index 从列表中找出某个值第一个匹配的索引值
list8 = [1, 2, 3, 4, 4, 5, 6]
index8 = list8.index(4)
# 圈定范围
index9 = list8.index(4, 4, 6)
print(index8, index9)

# 获取list的长度
print(len(list8))

# 获取列表最大值
print(max(list8))

# 最小值
print(min(list8))

# 查看元素在列表中出现的次数
list10 = [1, 2, 3, 3, 4, 5, 3, 5, 10]
print(list10.count(3))

# 删除所有的数据3
for i in range(0, list10.count(3)):
    list10.remove(3)
print(list10)

# reverse 倒序
list11 = [6, 2, 3, 4, 5]
list11.reverse()
print(list11)

# 排序
list11.sort()
print(list11)


# 拷贝
# 浅拷贝——引用拷贝
list1 = [1, 2, 3]
list2 = list1
list2[0] = 3
print(id(list1), id(list2))
print(list1, list2)

# 深拷贝——内存拷贝
list3 = [1, 2, 3]
list4 = list3.copy()
list4[0] = 2
print(id(list3), id(list4))
print(list3, list4)

# 元祖转换成列表
list31 = list((2, 3, 3))
print(list31)

