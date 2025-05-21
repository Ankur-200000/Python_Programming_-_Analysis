import turtle as t
from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        x = 0
        for _ in range(3):
            self.add_segment(x, 0)
            x -= 20

    def add_segment(self, x, y):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.teleport(x, y)
        self.segments.append(new_segment)

    def extend(self):
        if self.tail.heading() == RIGHT:
            a = self.tail.xcor() - 20
            b = self.tail.ycor()
        elif self.tail.heading() == LEFT:
            a = self.tail.xcor() + 20
            b = self.tail.ycor()
        elif self.tail.heading() == UP:
            a = self.tail.xcor()
            b = self.tail.ycor() - 20
        elif self.tail.heading() == DOWN:
            a = self.tail.xcor()
            b = self.tail.ycor() + 20

        self.add_segment(a, b) #whichever if or elif statement passes, will now create a new turtle which teleports to its respective (a, b) coordinates
        self.tail = self.segments[-1] #update the tail

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):  # (i start value, i stop value, i step value)
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)
