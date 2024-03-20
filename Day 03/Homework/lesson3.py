from turtle import *

width(5)
speed(10)
#Step 1: Drawing a Square

color("black")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

#Step 2: Drawing a door

left(90)
forward(70)
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#Step 3: Drawing a roof

penup()
goto(200,200)
pendown()
color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#Step 4: Drawing Windows

penup()
goto(40,170)
pendown()

begin_fill()
color("grey")
left(30)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
end_fill()

penup()
goto(140,170)
pendown()

begin_fill()
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
end_fill()
exitonclick()



#Sky
penup()
goto(-400, -100)
pendown()
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()


