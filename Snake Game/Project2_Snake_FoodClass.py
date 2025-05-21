from turtle import Turtle
import random

class Food(Turtle): #adds the circle
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.teleport(random.randint(-280, 280), random.randint(-280, 280))
