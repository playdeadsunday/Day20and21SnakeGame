from turtle import Turtle
STYLE = ('Courier', 14, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', font=STYLE, align=ALIGNMENT)

    def increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def end_of_game(self):
        self.goto(0, 0)
        self.write('GAME OVER :(', font=STYLE, align=ALIGNMENT)