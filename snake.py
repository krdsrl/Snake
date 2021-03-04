import turtle
import time
from random import *


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


def gyumolcs_kirak():
    x = randint(-380, 380)
    y = randint(-280, 280)
    gyumolcs.goto(x, y)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(jobbra, "Right")
palya.onkey(balra, "Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

gyumolcs = turtle.Turtle()
gyumolcs.penup()
gyumolcs.shape("circle")
gyumolcs.color("red")
gyumolcs_kirak()


kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.goto(-25, 250)

kijelzo2 = turtle.Turtle()
kijelzo2.color("white")
kijelzo2.hideturtle()
kijelzo2.penup()
kijelzo2.goto(-25, 50)
a=0
kijelzo2.write(f"Pont: 0", font=("Arial", 16, "bold"))

while True:
    fej.forward(20)
    if fej.distance(gyumolcs.xcor(), gyumolcs.ycor()) < 15:
        gyumolcs_kirak()
        a+=1
        kijelzo2.clear()
        kijelzo2.write(f"Pont: {a}", font=("Arial", 16, "bold"))
    if fej.xcor() > 400 or fej.xcor() < -400 or fej.ycor() > 300 or fej.ycor() < -300:
        kijelzo.write("Megdöglött a kukac", font=("Arial", 16, "bold"))
    time.sleep(0.3)
    palya.update()
