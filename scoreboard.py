from turtle import Turtle

FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-280, y=260)
        self.level = 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER :(", align="center", font=FONT)
