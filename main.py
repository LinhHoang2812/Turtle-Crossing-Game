import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()



car_manager = CarManager()

scoreboard=Scoreboard()


screen.listen()
screen.onkey(key="Up",fun=player.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    car_manager.add_new_car()
    for car in car_manager.all_car:
        if player.distance(car.position()) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= 280:
        player.reset()
        car_manager.speed += 5
        scoreboard.level += 1
        scoreboard.update_level()












screen.exitonclick()