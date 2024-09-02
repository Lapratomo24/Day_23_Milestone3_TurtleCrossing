from turtle import Turtle
import random

color_tuples = [(246, 246, 241), (29, 101, 154), (181, 63, 28), (249, 168, 83),
                (186, 45, 111), (218, 211, 62), (242, 210, 215), (233, 244, 238),
                (243, 154, 185), (122, 205, 188), (146, 196, 3), (175, 120, 155),
                (170, 204, 191), (4, 127, 70), (252, 95, 6), (236, 243, 249),
                (253, 196, 0), (205, 16, 94), (2, 121, 66), (169, 104, 140)]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(180)
        self.color("red")
        self.setx(280)
        self.sety(200)
        self.x_move = 10

    def move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, y=200)
