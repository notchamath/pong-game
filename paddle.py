from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, pos):
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.setpos(pos)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
