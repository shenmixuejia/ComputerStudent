# coding=gbk
"""
作者：川川
公众号：玩转大数据
@时间  : 2022/2/3 0:49
群：428335755
"""
import turtle
import math
turtle.pen()
t=turtle
t.up()
t.goto(0,150)
t.down()
t.color('red')
t.begin_fill()
t.fillcolor('red')
t.speed(1)
t.left(45)
t.forward(150)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(250+math.sqrt(2)*100)
t.right (90)
t.speed(2)
t.forward(250+100*math.sqrt(2))
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(150)
t.end_fill()
t.goto(-10,0)
t.pencolor('white')
#L
t.pensize(10)
t.goto(-50,0)
t.goto(-50,80)
t.up ()
#I
t.goto(-100,0)
t.down()
t.goto(-160,0)
t.goto(-130,0)
t.goto(-130,80)
t.goto(-160,80)
t.goto(-100,80)
t.up()
#O
t.goto(10,25)
t.down()
t.right(45)
t.circle(25,extent=180)
t.goto(60,55)
t.circle(25,extent=180)
t.goto(10,25)
t.up()
t.goto(75,80)
t.down()
t.goto(100,0)
t.goto(125,80)
t.up()
t.goto(180,80)
t.down()
t.goto(140,80)
t.goto(140,0)
t.goto(180,0)
t.up()
t.goto(180,40)
t.down()
t.goto(140,40)
#U
t.up()
t.goto(-40,-30)
t.down()
t.goto(-40,-80)
t.circle(40,extent=180)
t.goto(40,-30)
t.hideturtle()