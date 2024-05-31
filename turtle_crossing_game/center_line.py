from turtle import Turtle

class Centerline(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.width(3)
        self.penup()
        self.goto(x, y)
        self.pendown()
        for i in range(20):
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(15)