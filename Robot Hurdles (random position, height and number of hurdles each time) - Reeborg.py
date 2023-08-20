def turn_right():
    {turn_left()}, {turn_left()}, {turn_left()}
       
def jump_and_go():
    {turn_left()}
    while not right_is_clear():
        move()
    else:
        {turn_right()}, {move()}, {turn_right()}
        while front_is_clear():
            move()
        else:
            turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_and_go()







#Conditions: front_is_clear() / at_goal() / right_is_clear()