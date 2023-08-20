from turtle import Turtle

# ------------------------------ Create Objects ------------------------------ #

class Paddle(Turtle):
    def __init__(self, setx_param):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, .3)
        self.penup()
        self.setx(setx_param) #need to input -350

    # --------------------------------- Functions -------------------------------- #

    def right_paddle_up_movement(self):
        self.sety(self.ycor() + 60)


    def right_paddle_down_movement(self):
        self.sety(self.ycor() - 60)

    
    def left_paddle_up_movement(self):
        self.sety(self.ycor() + 60)


    def left_paddle_down_movement(self):
        self.sety(self.ycor() - 60)