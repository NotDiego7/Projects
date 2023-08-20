from turtle import Turtle
import random

class Snake:
    def __init__(self):
        # ---------------------------- Object construction --------------------------- #
        self.snake_part_one = Turtle()
        self.snake_part_two = Turtle()
        self.snake_part_three = Turtle()

        self.snake_part_list = [self.snake_part_one, self.snake_part_two, self.snake_part_three]
        # -------------------------------- Properties -------------------------------- #

        start_point = 0
        for part in self.snake_part_list:
            part.shape(name="square")
            part.color("white")
            part.penup()
            part.setx(start_point)
            part.speed("slowest")
            start_point -= 20

    # --------------------------------- Functions -------------------------------- #

    def go_right(self):
        if self.snake_part_one.heading() != 180:
            self.snake_part_one.setheading(0)


    def go_up(self):
        if self.snake_part_one.heading() != 270:
            self.snake_part_one.setheading(90)


    def go_left(self):
        if self.snake_part_one.heading() != 0:
            self.snake_part_one.setheading(180)


    def go_down(self):
        if self.snake_part_one.heading() != 90:
            self.snake_part_one.setheading(270)

    # ------------------------ Set Simultaneous Movements ------------------------ #

    def head_movement(self):
        for angle in range(0, 360, 90):
            if self.snake_part_one.heading() == angle:
                one_x = self.snake_part_one.xcor()
                one_y = self.snake_part_one.ycor()
                self.snake_part_one.forward(20)

    def body_movement(self):
        for part in range(len(self.snake_part_list) - 1, 0, -1):
            x = self.snake_part_list[part - 1].xcor()
            y = self.snake_part_list[part - 1].ycor()
            self.snake_part_list[part].goto(x, y)

    def add_extension(self):
        self.snake_part_list.append(self.snake_part_list[-1].clone())

    def reset_snake(self):
        for i in self.snake_part_list:
            i.hideturtle()
        self.snake_part_list.clear()

        # ----------------------- Initializing again, basically ---------------------- #
        
        self.snake_part_one = Turtle()
        self.snake_part_two = Turtle()
        self.snake_part_three = Turtle()

        self.snake_part_list = [self.snake_part_one, self.snake_part_two, self.snake_part_three]

        start_point = 0
        for part in self.snake_part_list:
            part.shape(name="square")
            part.color("white")
            part.penup()
            part.setx(start_point)
            part.speed("slowest")
            start_point -= 20
