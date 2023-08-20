# -------------------------- Getting colors in image ------------------------- #

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))

# print(rgb_colors)

# ------------------------ Colors in image (- whites) ----------------------- #

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), 
(54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 
153), (176, 192, 208), (168, 99, 102)]

refactored_color_list = []

for tuple in color_list:
    if tuple[0] < 235 and tuple[1] < 235 and tuple[2] < 235:
        refactored_color_list.append(tuple)

# ---------------------------------- Imports --------------------------------- #

from turtle import Turtle, Screen
import random
# ---------------------------- Object construction --------------------------- #

base_point = Turtle()
screen = Screen()

# ----------------------------------- Setup ---------------------------------- #

screen.screensize(1600, 1200)
screen.setup(1600, 900)
screen.colormode(255)
base_point.pensize(1)
base_point.shape("triangle")
base_point.speed(10)

# --------------------------------- Functions -------------------------------- #

def render_painting():
    for dot in range(10):
        random_color = random.choice(refactored_color_list)
        base_point.setheading(0)
        base_point.dot(15, random_color)
        base_point.penup()
        base_point.forward(50)
        

def move_pen_upward(x_param, y_param):
        for i in range(10):
            y_param += 50
            base_point.goto(x_param, y_param)
            return y_param


# --------------------------------- Main Flow -------------------------------- #
x = 0
y = 0
for i in range(10):
    base_point.hideturtle()
    render_painting()
    y = move_pen_upward(x, y)



screen.exitonclick()