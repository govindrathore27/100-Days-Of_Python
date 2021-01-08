from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def score_counter(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Ariel", 24, "bold"))
