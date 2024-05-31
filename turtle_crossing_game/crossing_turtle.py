from turtle import Turtle

class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setheading(90)

    def reset_fun(self):
        self.goto(0, -160)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)