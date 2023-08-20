from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.x = 10
        self.y = 10


    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x, y + self.y)


    def wall_bounce(self):
        self.y *= -1

    
    def paddle_bounce(self):
        # self.increase_speed()
        self.x *= -1
                

    def reset(self):
        self.home()
        self.x *= -1