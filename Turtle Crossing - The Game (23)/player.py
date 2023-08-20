from turtle import Turtle


class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.sety(-275)


    def move_up(self):
        self.sety(self.ycor() + 15)


    def got_finish_line(self):
        if self.ycor() > 290:
            return True

    
    def set_home(self):
        self.sety(-275)