import turtle
import pandas

states = []
score = 0

# ------------------------------- Screen Object ------------------------------ #

screen = turtle.Screen()

# ----------------------------- Screen Properties ---------------------------- #

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

# ----------------------------- Turtle Properties ---------------------------- #

turtle.penup()
turtle.hideturtle()

# -------------- CSV to usable object and states column to list -------------- #

states_data = pandas.read_csv(filepath_or_buffer="50_states.csv")

states = states_data["state"].to_list()

# --------------------------------- Functions -------------------------------- #

def prompt(score_param):
    if score_param == 0:
        player_guess = screen.textinput(title="Guess the state", prompt="Enter your guess to see if you're correct: ").title()
    else:
        player_guess = screen.textinput(title=f"{score_param}/50 States Guessed Correctly", prompt="Enter your guess to see if you're correct: ").title()
    return player_guess

# --------------------------------- Main Flow -------------------------------- #
ongoing_session = True

while ongoing_session:
    player_guess = prompt(score)
    if player_guess in states:
        current_state = states_data[states_data["state"] == player_guess]
        xcor = int(current_state["x"].iloc[0])
        ycor = int(current_state["y"].iloc[0])

        turtle.goto(xcor, ycor)
        turtle.write(arg=player_guess, move=False, align="center", font=("courier", 9, "bold"))

        # --------------------------- Record correct answer -------------------------- #

        states.remove(player_guess)

        # -------------- Keep track of Score (rendered on prompt window) ------------- #

        score += 1

        # ------------ If no more states list (player guessed all of them) ----------- #

        if len(states) == 0:
            ongoing_session = False

    # ------------------------------ Exit Condition ------------------------------ #

    elif player_guess == "Exit":
        break

# -------- Create a CSV file containing the states the player's missed ------- #

pandas.DataFrame(data=states, columns=["State"]).to_csv(path_or_buf="Missed states.csv")