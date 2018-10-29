# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/27 17:58
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import math
import random

a = 10
print(id(a))
a = 20
b = a
print(id(a), id(b))  # a地址改变，b与a相等
b = 30
print(id(a), id(b))  # a与b不同


# 连续定义多个变量
num1 = num2 = num3 = 1

# 交互式赋值定义变量
num4, num5 = 6, 17

print(num4, num5)
data = ['alex', 84, [1900, 3, 38]]
name, age, birth = data
print(name)
print(age)
print(birth)


"""
浮点数：运算可能会有四舍五入的误差
"""

f1 = 1.1
f2 = 2.2
print(f1 + f2)  # 结果为3.3000000000000003

"""
复数：实数部分和虚数部分组成
"""


"""
数字类型转换
"""

f1 = 1.8
print(int(f1))
print(int("123"))
print(float("12.3"))
print(int(float("12.3")))
print(int("+123"))
print(int("-123"))

x = -10
print(abs(x))
print((10 > 9)-(10 > 9))


# 返回最大值
print(max(1, 2, 3, 4, 5))
# 返回最小值
print(min(1, 2, 3, 4, 5))


# 2的4次方
print(pow(2, 4))

# round(x[,n])返回浮点数x，如果给出n值，则代表舍入到小数后n位
print(round(3.3))
print(round(3.5))
print(round(-3.3))
print(round(-3.5))
print(round(3.546, 2))
print(round(3.546, 1))


# 向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))

# 向下取整
print(math.floor(18.1))
print(math.floor(18.9))

# 返回小数部分（浮点数）与整数部分
print(math.modf(22.3))

# 平方根
print(math.sqrt(16))


# 随机数
# 1 从序列中随机选择一个元素
print(random.choice([1, 3, "aa"]))
print(random.choice(range(5)))  # range(5) = [0, 1, 2, 3, 4]
print(random.choice("ABCDE"))   # "ABCDE" = ["A", "B", "C", "D", "E"]

# 2 产生一个1~100的随机数
r1 = random.choice(range(1, 101, 1))
r2 = random.choice(range(100))+1
print(r1, r2)

# 3 randrange ([start,] stop [,step]) 与range类似，返回的是值，而range是数组
r3 = random.randrange(1, 100, 3)
print(r3)

# 4 随机产生[0,1）的浮点数
print(random.random())


# 将列表的元素随机排列
list2 = [0, 1, 2, 3, 4]
random.shuffle(list2)

#
list3 = random.sample(list2, 3)
print(list2)
print(list3)

# 随机生成一个实数 [x, y) 范围内
print(random.uniform(3, 3))

