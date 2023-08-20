from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard

# ---------------------------- Object construction --------------------------- #

snake = Snake()
screen = Screen()
food = Food()
score = Scoreboard()

# ----------------------------------- Setup ---------------------------------- #

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(n=0)

screen.listen()
screen.onkey(fun=snake.go_right, key="Right")
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_left, key="Left")
screen.onkey(fun=snake.go_down, key="Down")

# ------------------------------- Set Recursion ------------------------------ #

game_on = True

while game_on:
        score.get_score()
        snake.head_movement()
        snake.body_movement()
        screen.update()
        sleep(.055)

        if food.distance(snake.snake_part_one) < 18:
            snake.add_extension()
            score.add_to_score()
            food.refresh()

    # ----------------------------------- Day 2 ---------------------------------- #

        if snake.snake_part_one.xcor() > 280 or snake.snake_part_one.xcor() < -280 or snake.snake_part_one.ycor() > 280 or snake.snake_part_one.ycor() < -280:
            snake.reset_snake()
            score.reset_score()

        for part in snake.snake_part_list[2:]:    
            if snake.snake_part_list[0].distance(part) < 10:
                snake.reset_snake()
                score.reset_score()

screen.exitonclick()