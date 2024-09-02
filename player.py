from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=0, y=new_y)