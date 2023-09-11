from turtle import Turtle
score = 0

class Score_Board(Turtle):

    def __init__(self,score):
        super().__init__()
        self.penup()
        self.score = score
        self.goto(-250, 155)
        self.hideturtle()
        self.color("Black")
        self.speed("fastest")
        self.write(f"score: {self.score}", move=False, align="center", font=("Arial", 15, "normal"))