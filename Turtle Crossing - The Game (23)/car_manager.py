from turtle import Turtle
from random import choice, randrange, randint

# --------------------------------- Constants -------------------------------- #

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = []


class Car(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.setheading(180)
        self.setx(330)
        self.sety(randrange(-215, 225, 20))

    def x_axis_movement(self):
        self.setx(self.xcor() - 7)


class CarManager(Car):
    def __init__(self):
        super().__init__()

        self.cars_list = []

    
    def clear_cars(self):
        for i in range(len(self.cars_list)):
            self.cars_list[i].reset()
            self.cars_list[i].hideturtle()

        self.cars_list.clear()
        


