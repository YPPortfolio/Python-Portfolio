from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

#login of all the cars continuing to move: car is created using car_generation function, which adds a car to the cars list.
#car_move function goes through the cars list to move car by the speed amount, which repeats in the while loop in main.py
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def car_generation(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(290, random.randint(-260, 260))
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.fd(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
