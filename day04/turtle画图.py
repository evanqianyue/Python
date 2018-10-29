# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/10/29 11:48
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""
# 运动命令
# forward()
# backward()
# right()向右旋转多少度
# left()向左旋转多少度
# goto()移动到坐标x,y的位置
# speed() 绘制速度 范围[0,10]

# 笔画控制命令
# up() 抬起画笔
# down() 落下画笔
# setheading(d) 改变海龟的朝向
# pensize(d) 笔画宽度
# pencolor(colorstr) 笔画颜色
# reset() 恢复所有设置，清空窗口，重置turtle
# clea() 清空窗口
# circle(r,steps) r半径 steps次数  (默认为圆圈，3为三角形)


# begin_fill()
#
# end_fill()
# 其他命令
# done() 继续执行
# undo() 撤销上一次动作
# hideturtle() 显示海龟
# showturtle() 隐藏海龟
# screensize(x,y) 屏幕大小

import turtle

turtle.screensize(500, 400, "pink")
turtle.speed(10)
turtle.forward(100)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.left(90)
turtle.backward(100)
turtle.pensize(5)
turtle.goto(100, 200)
turtle.clear()
turtle.forward(100)
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(50, steps=5)
turtle.end_fill()
turtle.hideturtle()
turtle.done()

