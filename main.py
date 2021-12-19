from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game.")

x_pos = 0

segments = []
for _ in range(3):
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.goto(x_pos, 0)
    new_segment.color("white")
    segments.append(new_segment)
    x_pos -= 20


screen.exitonclick()
