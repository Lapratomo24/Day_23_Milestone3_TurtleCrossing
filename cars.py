from turtle import Turtle
import random

colors = ["red", "orange", "grey", "green", "blue", "purple"]


class Cars:
    def __init__(self):
        self.cars = []

    def spawn_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            y_pos = random.randint(-250, 250)
            new_car.goto(300, y_pos)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(10)
