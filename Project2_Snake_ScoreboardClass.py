from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGN = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align= ALIGN, font=FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write(f"Game Over!\nFinal Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
