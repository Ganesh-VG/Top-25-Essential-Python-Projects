from turtle import Turtle

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 150)
        self.hideturtle()
        self.color("Black")
        self.speed("fastest")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 20, "normal"))