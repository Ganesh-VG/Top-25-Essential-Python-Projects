import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super(). __init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.goto(-150, 150)

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
