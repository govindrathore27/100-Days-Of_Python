import turtle as t
import random
import colorgram

tim = t.Turtle()
t.colormode(255)
t.hideturtle()
tim.hideturtle()
t.speed("fastest")
tim.setheading(255)
number_of_dots = 100
tim.penup()
tim.forward(300)
tim.setheading(0)
colors = colorgram.extract("hirst.jpg",25)
rgb_colors = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color= (r,g,b)
    rgb_colors.append(new_color)
for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()