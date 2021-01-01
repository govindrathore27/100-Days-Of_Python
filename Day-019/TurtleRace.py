from turtle import Turtle , Screen
import random

colors = ['red','blue','green','yellow','purple']

turtles = {}
for i in colors:
    turtles[i] = Turtle("turtle")
is_game_on = False
screen = Screen()
screen.setup(width=600,height=400)
user_bet = screen.textinput(title="Place your bets",prompt="Which turtle will win the race? Enter the color :")

for i in range(len(colors)):
    turtles[colors[i]].color(colors[i])
    turtles[colors[i]].penup()
    turtles[colors[i]].goto(-260,-150 + i*80)
if user_bet:
    is_game_on = True
f = 0
while is_game_on:
    for i in turtles:
        if turtles[i].xcor() > 280:
            is_game_on = False
            winning_color = turtles[i].pencolor()
            if winning_color == user_bet:
                f = 1
        random_distances = random.randint(0,20)
        turtles[i].forward(random_distances)

for i in turtles:
    turtles[i].hideturtle()

if f == 1:
    print(f"Wow!! You won the bet.Winning color is {winning_color}")

    turtles[i].clear()
    turtles[i].goto(-190,0)
    turtles[i].write(f"Wow!! You won the bet.Winning color is {winning_color}", font=("Arial", 16, "normal"))
else:
    print(f"Oopsie!!! You lost the bet.Winning color is {winning_color}")
    turtles[i].clear()
    turtles[i].goto(-190,0)
    turtles[i].write(f"Oopsie!! You lost the bet.Winning color is {winning_color}", font=("Arial", 16, "normal"))

screen.exitonclick()