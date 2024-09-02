from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=270)
        self.display_score()

    def display_score(self):
        self.write(f"LEVEL: {self.level}", False, align="left")