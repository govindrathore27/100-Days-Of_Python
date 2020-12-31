import turtle
import random
timmy = turtle.Turtle()
colors = ["medium blue","firebrick","dark slate blue","violet","green yellow"]
for i in range(3,10):
    timmy.pencolor(random.choice(colors))
    for _ in range(i):
        timmy.forward(100)
        timmy.left(360/i)

screen = turtle.Screen()
screen.exitonclick()