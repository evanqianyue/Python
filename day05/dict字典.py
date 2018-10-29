# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 14:09
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

"""
使用键-值存储，具有极快的速度
注意：字典是无序的

key的特性：
1、字典中的key必须唯一
2、key必须是不可变对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变，不能作为key

"""


json = {"tom": 120, "evan": 99, "tim": 88,"HC": 95}

# 元素的访问
# 获取：字典名[key]

print(json["tom"])
print(json.get("tom"))
print(json.get("jack"))  # None

# 添加 / 修改
json["hanmeimei"] = 90
json["evan"] = 85  # 若已存在，则更新key：evan对应的值

# 删除
json.pop("tom")
print(json)

# 遍历
for key in json:
    print(key, json[key])

print("json.values:", json.values())

for value in json.values():
    print(value)

for k, v in json.items():
    print(k, v)

for i, v2 in enumerate(json):
    print(i, v2)


# 和list比较
# 1、查找和插入的速度极快，不会随着key-value的增加而变慢
# 2、需要占用大量的内容，浪费内存少

# list
# 查找和插入的速度随着数据量的增多而减慢
# 占用空间小，浪费内存多
