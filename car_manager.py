import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle

class CarManager:
    def __init__(self):


        self.all_car = []

        self.loop_count = 0

        self.speed= 0
        self.create_car()



    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        pos_y= random.randint(-250,250)
        car.goto(300, pos_y)

        self.all_car.append(car)

    # def make_car(self):
    #     for _ in range(11):
    #         pos_y = random.randint(-250,250)
    #         pos_x = random.randint(0,280)
    #         self.create_car(pos_x,pos_y)


    def add_new_car(self):
        if self.loop_count % 6 == 0:
            self.create_car()

    def move(self):
        for car in self.all_car:
            car.forward(STARTING_MOVE_DISTANCE + self.speed)

        self.loop_count += 1



