from turtle import Turtle, colormode
import random

colormode(255)
color_list_1 = [(45, 97, 147), (168, 49, 80), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78)]

class Car(Turtle):
    def __init__(self):
        super(). __init__()
        self.y = random.choice(range(-140, 150, 10))
        self.x = random.choice(range(300, 900, 40))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=1)

    def create_car(self):
        self.color(random.choice(color_list_1))
        if self.y == -50 or self.y == 50:
            pass
        else:
            self.goto(self.x, self.y)


