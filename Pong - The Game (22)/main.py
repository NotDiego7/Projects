from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import ScoreRight, ScoreLeft

# ----------------------------------- Vars ----------------------------------- #

sleep_time = .045

# ------------------------------- Screen Object ------------------------------ #

screen = Screen()

# ----------------------------- Screen Properties ---------------------------- #

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# ------------------------------- Game Objects ------------------------------- #

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
score_right = ScoreRight()
score_left = ScoreLeft()

# ------------------------------- Right Paddle ------------------------------- #

screen.onkeypress(key= "Up", fun= right_paddle.right_paddle_up_movement)
screen.onkeypress(key= "Down", fun= right_paddle.right_paddle_down_movement)

# -------------------------------- Left Paddle ------------------------------- #

screen.onkeypress(key= "w", fun= left_paddle.left_paddle_up_movement)
screen.onkeypress(key= "s", fun= left_paddle.left_paddle_down_movement)

# ----------------------------------- Flow ----------------------------------- #

ongoing_game = True
while ongoing_game:   
    ball.move()
    
    if ball.ycor() < -275 or ball.ycor() > 275:
        ball.wall_bounce()
    

    if ball.xcor() > 338 or ball.xcor() < -338:
        if ball.distance(right_paddle) < 60 or ball.distance(left_paddle) < 60:
            ball.paddle_bounce()
            if sleep_time > .02:
                sleep_time -= .004


    if ball.xcor() > 370:
        score_left.get_left_score()
        ball.reset()
        sleep_time = .045
    elif ball.xcor() < -370:
        score_right.get_right_score()
        ball.reset()
        sleep_time = .045

    screen.update()
    sleep(sleep_time)





screen.exitonclick()