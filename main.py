from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game.")
screen.tracer(0)

snake = Snake()
screen.listen()

is_game = True
while is_game:
    screen.update()
    time.sleep(0.06)

    snake.move()

    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

screen.exitonclick()
