import turtle
from turtle import Turtle
import random

turtle.colormode(255)
LANES_Y_S = [-250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100,
             -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130,
             140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


class Cars:

    def __init__(self):
        self.total_cars_num = 20
        self.cars_list = []
        self.active_cars_list = []

    def create_cars(self):
        for car in range(self.total_cars_num):
            car = Turtle(shape="square")
            random_color = generate_color()
            car.color(random_color)
            car.penup()
            car.setheading(180)
            car.goto(320, random.choice(LANES_Y_S))
            car.shapesize(stretch_len=2)
            self.cars_list.append(car)

    def refresh_active_cars(self):
        active_cars_num = random.randint(0, 1)
        for _ in range(active_cars_num):
            car = random.choice(self.cars_list)
            self.active_cars_list.append(car)
