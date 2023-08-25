from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        heading = random.randint(0, 360)
        self.setheading(heading)
        self.forward(100)
