from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.spawn_cars()
    cars.move()

    # detect the "finish line"
    if player.ycor() > 250:
        player.respawn()
        cars.next_level()

    # detect collision with a car
    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()