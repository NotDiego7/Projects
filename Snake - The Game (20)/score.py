from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(260)
        
        self.score = 0

    
    def get_score(self):
        with open("data.txt") as data_file:
            self.highscore = int(data_file.read())

        self.clear()
        self.write(f"Score: {self.score}            Highscore: {self.highscore}", False, "center", ("Courier ", 22, "normal"))

    def add_to_score(self):
        self.score += 1
        self.get_score()

    def reset_score(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as data_file:
                data_file.write(str(self.score))

        self.score = 0
        self.get_score()