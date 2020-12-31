import turtle as t
import random

tim = t.Turtle()
movement = [0,90,180,270]
tim.pensize(3)
t.colormode(255)
tim.speed(30)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
for _ in range(200):
    t.color(random_color())
    tim.setheading(random.choice(movement))
    tim.forward(10)



screen = t.Screen()
screen.exitonclick()