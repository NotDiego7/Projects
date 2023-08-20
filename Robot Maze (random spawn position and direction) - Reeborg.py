def turn_right():
    turn_left(), turn_left(), turn_left()
def left_is_clear():
    right_is_clear(), right_is_clear(), right_is_clear()

def conditions():
    if right_is_clear() and left_is_clear():
        move()
    elif right_is_clear():
        turn_right(), move()
    elif front_is_clear():
        move()
    else:
        turn_left()

while not at_goal():
    conditions()

#added the and left_is_clear() to line 7 and the created the function for it too since we had an edge case infinate loop