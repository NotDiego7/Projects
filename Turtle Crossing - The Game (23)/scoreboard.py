from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-200, 250)
    
    
    def get_level(self):
        self.write(arg=f"Level: {self.score}", move= False, align= "center", font=FONT)

    
    def up_level(self):
        self.clear()
        self.score += 1

    
    def game_over(self):
        self.home()
        self.write(arg=f"Turtle's been hit!\nGame Over!", move= False, align= "center", font=FONT)
