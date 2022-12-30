from turtle import Turtle

class States_Written(Turtle):
    
    def __init__(self, name, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.write(name, align="center", font=("Courier", 10, "normal"))