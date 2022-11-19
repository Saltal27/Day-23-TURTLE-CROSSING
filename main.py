from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

puck = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=puck.move_up, key="Up")
screen.onkey(fun=puck.move_down, key="Down")
screen.onkey(fun=puck.move_left, key="Left")
screen.onkey(fun=puck.move_right, key="Right")

movement_speed = 0.09
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(movement_speed)
    cars.create_cars()
    cars.refresh_active_cars()

    for car in cars.active_cars_list:
        if car.xcor() > - 320:
            car.forward(random.randint(10, 20))
            if car.distance(puck) < 30 and car.ycor() - 10 < puck.ycor() < car.ycor() + 10\
                    or car.distance(puck) < 20:
                game_is_on = False
                scoreboard.game_over()
        else:
            car_y = car.ycor()
            car.goto(320, car_y)
            cars.active_cars_list.remove(car)

    if puck.ycor() >= 260:
        scoreboard.level += 1
        scoreboard.refresh_scoreboard()
        puck.goto(0, -280)
        movement_speed *= 0.9


screen.exitonclick()
