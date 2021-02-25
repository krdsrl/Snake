import turtle
import time

palya = turtle.Screen()
palya.setup(width=800,height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

while True:
    fej.forward(20)
    palya.update()
    time.sleep