import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

cars = []
i = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Check if player has completed the level
    if player.ycor() > 290:
        scoreboard.increase_level()
        player.reset()

    # Create a new car and append to the car list
    if i % (11-scoreboard.level) == 0:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.move_car(scoreboard.level)
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    i += 1

screen.exitonclick()
