from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game.")

x_pos = 0
for _ in range(3):
    new_turtle = Turtle("square")
    new_turtle.goto(x_pos, 0)
    new_turtle.color("white")
    x_pos -= 20

screen.exitonclick()
