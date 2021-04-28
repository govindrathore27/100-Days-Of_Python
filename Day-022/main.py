from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)
l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50  and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50  and ball.xcor() < -320:
        ball.bounce_x()
    # Detect the paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()