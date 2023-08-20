from turtle import Turtle
#TODO: There was no need for the second classs

class ScoreRight(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setx(60)        
        self.sety(250)
        self.right_score = 0


    def get_right_score(self):
        self.right_score += 1
        self.clear()
        self.setx(60)
        self.write(f"{self.right_score}", False, "center", ("verdana", 30, "bold"))


class ScoreLeft(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setx(-60)
        self.sety(250)
        self.left_score = 0

    def get_left_score(self):
        self.left_score += 1
        self.clear()
        self.write(f"{self.left_score}", False, "center", ("verdana", 30, "bold"))