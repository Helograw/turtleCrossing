import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

level = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move(level)

    for individual_car in car.all_cars:
        if individual_car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > 290:
        level += 1
        scoreboard.update_score()
        player.reset()

scoreboard.game_over()

screen.exitonclick()
