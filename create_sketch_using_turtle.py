# from sketchpy import canvas
# import turtle
# obj=canvas.sketch_from_image("C:\\Users\\HP\\pradip1.jpg")
# t=turtle.Turtle()
# t.penup()
# t.goto(-60,-290)
# t.pendown()
# t.pencolor("#ff6600")
# t.write("Happy Coding!", align="center", font=("arial",30,))
# obj.draw()
# t.hideturtle()
# turtle.done()

from turtle import *
from random import randint
speed(0)
bgcolor("black")
i=1
while i<450:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    fd(50+i)
    rt(91)
    i+=1
exitonclick()