import turtle
# everything that comes after the # is a comment.
#it is a note to the person reading the code.
#the computer ignores it.
#write your code below here...

turtle.penup() #pick up the pen so it doesn't draw
turtle.goto(-200,-100)  #put the pen down to start
#drawing,
#draw the M
turtle.pendown()
turtle.goto (-200,-100+200)
turtle.goto (-200+50,-100)
turtle.goto (-200+100,-100+200)
turtle.goto (-200+100,-100)
#now lets draw an E
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(120,100)
turtle.goto(0,100)

turtle.goto(0,-100)
turtle.goto(0,0)
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(120,100)
turtle.goto(0,100)

turtle.goto(0,-100)
turtle.goto(0,0)

turtle.goto(120,0)
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.goto(120,-100)

#now lets draw another E

turtle.penup()
turtle.goto(200,100)
turtle.pendown()
turtle.goto(320,100)
turtle.goto(200,100)

turtle.goto(200,-100)
turtle.goto(200,0)
turtle.penup()
turtle.goto(200,100)
turtle.pendown()
turtle.goto(320,100)
turtle.goto(200,100)

turtle.goto(200,-100)
turtle.goto(200,0)

turtle.goto(320,0)
turtle.penup()
turtle.goto(200,-100)
turtle.pendown()
turtle.goto(320,-100)
#now it's time to draw T
turtle.penup()
turtle.goto(370,0)
turtle.pendown()
turtle.goto(470,0)
turtle.goto(235,0)
turtle.goto(235,-200)















#now lets draw the other E
#...and end it before the next line.
turtle.mainloop()
