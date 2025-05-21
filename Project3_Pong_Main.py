import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scores import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800,600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

n = 0.1
game_is_on = True
while game_is_on:
    time.sleep(n)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) <= 61 and ball.xcor() > 330 or ball.distance(l_paddle) <= 61 and ball.xcor() < -330:
        ball.bounce_x()
        if n <= 0.018531:
            n = 0.018531
        else:
            n *= 0.9 #speeds up ball
        # ball is 10 units in radius and paddle is 10 units in thickness from centre to side.
        # So -20 from the paddle x.cor() gives 330 as paddle collision x.cor()
        # diagonal distance from centre of paddle to a corner is approx 51 units, and it's 10 units for the ball
        # So ideal distance from paddle should be 61 units or less given the x.cor() is 330

    elif ball.xcor() > 380:
        ball.home()
        ball.bounce_x()
        score.increase_score_left()
        n = 0.1 #reinitialize speed after point gain/loss

    elif ball.xcor() < -380:
        ball.home()
        ball.bounce_x()
        score.increase_score_right()
        n = 0.1

screen.exitonclick()
