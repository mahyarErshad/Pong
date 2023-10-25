from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.leftScore = 0
        self.rightScore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-100, 200)
        self.write(self.leftScore, align="center", font=("courier", 40, "normal"))