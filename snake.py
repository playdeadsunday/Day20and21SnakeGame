from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color("white")
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[i-1].xcor()
            next_y = self.segments[i-1].ycor()
            self.segments[i].goto(next_x, next_y)
        self.head.forward(MOVING_DISTANCE)

    def go_up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def go_down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def go_left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def go_right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
