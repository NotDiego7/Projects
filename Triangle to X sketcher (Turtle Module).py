from turtle import Turtle, Screen
from random import randint 

# --------------------- Constructing objects from classes -------------------- #

base_point = Turtle()
screen = Screen()

# ---------------------------- Setting up details ---------------------------- #

screen.screensize(4000, 2000, "black")
screen.setup(1600, 900)
base_point.pensize(1.7)
base_point.pencolor("white")
base_point.shape("triangle")
base_point.speed(15)
screen.colormode(255)

# --------------------------------- Functions -------------------------------- #

def get_random_color():
    """Returns random_color needed to draw each shape."""
    RGB_list = []
    for i in range(3):
        number = randint(0, 255)
        RGB_list.append(number)
    random_color = base_point.color(RGB_list)
    return random_color

def get_shape_angle(shape_sides_param):
    """Returns shape_angle needed to turn after drawing a side."""
    shape_angle = 360 / shape_sides_param
    return shape_angle

def draw_shape(shape_sides_param, shape_angle_param):
    """Draws shape."""
    get_random_color()
    for i in range(shape_sides_param):
        base_point.forward(100)
        base_point.right(shape_angle_param)

# ----------------------------------- Flow ----------------------------------- #

shape_sides = 3
while shape_sides <= 45:
    random_color = get_random_color()
    shape_angle = get_shape_angle(shape_sides)

    draw_shape(shape_sides, shape_angle)

    shape_sides += 1



screen.exitonclick()