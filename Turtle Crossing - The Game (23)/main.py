from turtle import Screen
from player import PlayerTurtle
from car_manager import CarManager, Car
from scoreboard import Score
from random import randint
from time import sleep


# ---------------------------------- Objects --------------------------------- #

screen = Screen()
screen.tracer(0)

player_turtle = PlayerTurtle()
car_manager = CarManager()
score = Score()

# ----------------------------------- Setup ---------------------------------- #

screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor("black")


screen.onkeypress(key="Up", fun=player_turtle.move_up)

# --------------------------------- Main Flow -------------------------------- #
ongoing_game = True
correct_distance = True
time_var = 0.01



while ongoing_game:
    score.get_level()
    # ------------------------- Get car & add to car list ------------------------ #

    if correct_distance == True:
        car_manager.cars_list.append(Car())

    # --------------------- Movement for each car in car list -------------------- #

    for i in range(len(car_manager.cars_list)):
        if car_manager.cars_list[i].xcor() > -320:
            car_manager.cars_list[i].x_axis_movement()
        else:
            car_manager.cars_list[i].clear(), car_manager.cars_list[i].hideturtle()
    
    # ------------------------------ Check Collision ----------------------------- #

    for i in range(len(car_manager.cars_list)):
        if car_manager.cars_list[i].distance(player_turtle) < 30:
            score.game_over()
            ongoing_game = False
            break

    # -------------- Check there's enough spacing between car spawns ------------- #

    if car_manager.cars_list[-1].xcor() > 260:
        correct_distance = False
    else:
        correct_distance = True
    
    # -------------------------- Finish Line properties -------------------------- #

    if player_turtle.got_finish_line() and time_var > 0: #TODO: Only have ten levels due to time_var condition bug here
        time_var -= 0.001
        correct_distance = True
        score.up_level()
        
        car_manager.clear_cars()
        player_turtle.set_home()


        
    
    sleep(time_var)
    screen.update()








screen.exitonclick()



"""TODO:
Start (again):
    Player's turtle instance will spawn at home position (low on screen) and iterate through flow (again)

End:
    When turtle instance makes it to the top, the player has passed that level and can move to the next level (repeat)
"""