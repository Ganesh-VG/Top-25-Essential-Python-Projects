from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_Board
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score_Board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

scoreboard.scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 15:

        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or
            snake.segments[0].ycor() < -290):

        snake.reset_snake()
        scoreboard.reset()

    for seg in snake.segments[1:]:
        if snake.segments[0].position() == seg.position():

            snake.reset_snake()
            scoreboard.reset()

screen.exitonclick()
