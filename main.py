from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game.")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()

is_game = True
while is_game:

    screen.update()
    time.sleep(0.1)

    # detection of collision with food
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment()

    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

screen.exitonclick()
