from turtle import Turtle, Screen
from random import randint, randrange

# ----------------------------------- Data ----------------------------------- #

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

# --------------------- Constructing objects from classes -------------------- #

screen = Screen()

# ---------------------------- Setting up details ---------------------------- #

screen.screensize(300, 300)

# --------------------------------- Functions -------------------------------- #

def get_random_speed():
    """Returns a random speed."""
    random_speed = randint(1, 10)
    return random_speed


def start_racing(random_speed_param):
    for i in colors:
        random_speed = get_random_speed()
        turtle_dict.get(i).forward(random_speed)
        
        width_position = turtle_dict.get(i).pos()[0]
    
        if width_position > 360:
            winner_color = i
            return i
    
    return width_position


def get_turtles():
    turtle_dict = {}
    for name in colors:
        turtle_dict.update({name: Turtle()})
    return turtle_dict

# ---------------------------------------------------------------------------- #
#                                   Main Flow                                  #
# ---------------------------------------------------------------------------- #

user_guess = screen.textinput(title="Make your bet!", prompt="Who will win the race? Enter the color: ").lower()

x = -400
y = -100
turtle_dict = get_turtles()

# ------------------------------ Set Properties ------------------------------ #

for i in colors:
    turtle_dict.get(i).speed("slow")
    turtle_dict.get(i).penup()
    turtle_dict.get(i).shape("turtle")
    turtle_dict.get(i).color(i)
    turtle_dict.get(i).setheading(0)
    turtle_dict.get(i).goto(x, y)
    y += 50

# ----------------------------- Initiate the race ---------------------------- #

for i in range(150):
    width_position_or_winner_color = start_racing(get_random_speed)
    
    # ---------------------- Check if user_guess was correct --------------------- #

    if width_position_or_winner_color in colors:
        if user_guess == width_position_or_winner_color:
            screen.textinput(title="You've won!", prompt=f"The {width_position_or_winner_color} color wins!\nPress enter to exit.")
        else:
            screen.textinput(title="You've lost!", prompt=f"The {width_position_or_winner_color} color wins!\nPress enter to exit.")
        break



screen.exitonclick()