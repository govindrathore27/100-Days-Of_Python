from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    '''
    Function to move forward by 10 units.
    '''
    tim.forward(10)

def move_backward():
    '''
    Function to move backward by 10 units.
    '''
    tim.backward(10)


def turn_left():
    '''
    Function to rotate to left by 10 units.
    '''
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    '''
    Function to rotate to right by 10 units.
    '''
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    '''
    Function to clear screen .
    '''
    tim.clear()
    tim.reset()

screen = Screen()
screen.listen() #event listener.
screen.onkey(key="w",fun = move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun = turn_right)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key="c",fun=clear)
screen.exitonclick()