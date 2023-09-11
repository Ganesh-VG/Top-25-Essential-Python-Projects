from turtle import Turtle,Screen
from center_line import Centerline
from move_car import MoveCar
from score_board import Score_Board

screen = Screen()
screen.bgcolor("khaki")
screen.setup(width=600, height=360)
screen.title("Turtle Crossing")
screen.tracer(0)
centerline1 = Centerline(-300, -50)
centerline2 = Centerline(-300, 50)
centerline3 = Centerline(-300, -150)
centerline4 = Centerline(-300, 150)
move_car = MoveCar()
move_car.move_car()
screen.exitonclick()