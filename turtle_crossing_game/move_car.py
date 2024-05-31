from turtle import Turtle,Screen
from car import Car
from crossing_turtle import CrossingTurtle
from score_board import Score_Board
from game_over import GameOver
import time


crossing_turtle = CrossingTurtle()
screen = Screen()
cars = []
score_board = Score_Board(0)

j = 1
t = 0.2

crossing_turtle.reset_fun()
screen.listen()
screen.onkey(crossing_turtle.up, "Up")
screen.onkey(crossing_turtle.down, "Down")

class MoveCar():
    def __init__(self):
        self.game_is_on = True
        self.move_distance = 10
    def move_car(self):
        while self.game_is_on:

            a = 1
            for i in range(1, 30):
                while a < i:
                    car = Car()
                    car.create_car()
                    a += 1
                    cars.append(car)
            move_range = int(600/self.move_distance)
            for _ in range(move_range):
                for e in range(len(cars)):
                    if crossing_turtle.ycor() > 150:
                        global j
                        global t
                        global score_board
                        score_board.clear()
                        score_board = Score_Board(j)
                        crossing_turtle.reset_fun()
                        j += 1
                        t -= 0.02

                    if cars[e].distance(crossing_turtle) < 5:
                        self.game_is_on = False
                        game_over = GameOver()
                        game_over.game_over()
                        break

                    else:
                        cars[e].backward(self.move_distance)
                screen.update()
                time.sleep(t)
                if t < 0.08:
                    t = 0.2