import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_MANAGER = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
#lesson: make variable different name than each instance
car_manager = CarManager()


screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_generation()
    car_manager.car_move()

    #Detect reaching the end
    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_score()
        car_manager.increase_speed()

    #detect collision with a car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over_statement()




screen.exitonclick()
