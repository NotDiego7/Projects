from turtle import Turtle, Screen
from random import randint, randrange

# --------------------- Constructing objects from classes -------------------- #

base_point = Turtle()
screen = Screen()

# ---------------------------- Setting up details ---------------------------- #

screen.screensize(9000, 9000, "black")
screen.setup(1600, 900)
base_point.pensize(5)
base_point.pencolor("white")
base_point.shape("triangle")
base_point.speed(18)
screen.colormode(255)

# --------------------------------- Functions -------------------------------- #

def get_random_color():
    """Returns a random_color."""
    RGB_list = []
    for i in range(3):
        number = randint(0, 255)
        RGB_list.append(number)
    random_color = base_point.color(RGB_list)
    return random_color

def get_random_angle():
    """Returns a random_angle."""
    random_angle = randrange(0, 360, 90)
    return random_angle

def draw_shape():
    """Draws shape."""
    for i in range(1000):
        get_random_color()
        random_angle = get_random_angle()
        base_point.forward(100)
        base_point.setheading(random_angle)
    end_point = True
    return end_point

# ----------------------------------- Flow ----------------------------------- #

end_point = False
while end_point == False:
    end_point = draw_shape()



screen.exitonclick()