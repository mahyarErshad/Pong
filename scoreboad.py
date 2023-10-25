from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.leftScore = 0
        self.rightScore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align="center", font=("courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.rightScore, align="center", font=("courier", 40, "normal"))

    def left_score(self):
        self.leftScore += 1
        self.update_scoreboard()

    def right_score(self):
        self.rightScore += 1
        self.update_scoreboard()
