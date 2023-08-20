from turtle import Turtle, Screen
from random import randint, randrange

# --------------------- Constructing objects from classes -------------------- #

base_point = Turtle()
screen = Screen()

# ---------------------------- Setting up details ---------------------------- #

screen.screensize(2000, 1000, "black")
screen.setup(1600, 900)
base_point.pensize(2)
base_point.pencolor("white")
base_point.shape("triangle")
base_point.speed(15)
screen.colormode(255)

# --------------------------------- Functions -------------------------------- #
def get_random_color():
    random_color_list = []
    for i in range(3):
        random_color_list.append(randint(0, 255))
    return random_color_list


def draw_circle():
    """Draws circle."""
    heading_angle = 0
    for i in range(72):
        random_color = get_random_color()
        base_point.color(random_color)
        base_point.setheading(heading_angle)
        base_point.circle(200)
        heading_angle += 5

    end_point = True
    return end_point

# ----------------------------------- Flow ----------------------------------- #

end_point = False
while end_point == False:
    end_point = draw_circle()



screen.exitonclick()
