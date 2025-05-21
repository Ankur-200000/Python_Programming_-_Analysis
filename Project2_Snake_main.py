import time
from turtle import Screen
from snake_game_ankur import Snake
from food_ankur import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off the screen updates to speed up the animation

snake = Snake() #adss snake
food = Food() #adds food
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for square in snake.segments[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
