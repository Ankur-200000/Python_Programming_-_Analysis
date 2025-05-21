from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Left Player: {self.score_left}  |  Right Player: {self.score_right}", align=ALIGN, font=FONT)

    def increase_score_left(self):
        self.score_left += 1
        self.update_score()

    def increase_score_right(self):
        self.score_right += 1
        self.update_score()
