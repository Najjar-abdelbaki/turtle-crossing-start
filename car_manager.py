from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_st = STARTING_MOVE_DISTANCE


    def creat(self):
        if randint(1, 6) == 1:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            y_start = randint(-250, 250)
            car.goto(300, y_start)
            car.color(choice(COLORS))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_st)

    def level_up(self):
        self.move_st += MOVE_INCREMENT