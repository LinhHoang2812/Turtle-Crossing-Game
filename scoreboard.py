FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level= 1
        self.goto(-200, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}",False,align="center",font=("Courier", 20, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,align="center",font=FONT)
