from turtle import Turtle


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 260)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")

    def scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", move=False, align="center",
                   font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.scoreboard()

    def increase_score(self):
        self.score += 1
        self.scoreboard()
