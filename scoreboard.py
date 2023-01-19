from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-280, 250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(SCORE_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over_statement(self):
        self.goto(0, 0)
        self.write(f"Your Final Score is: {self.score}. Thank you for playing!", align="center", font=10)


