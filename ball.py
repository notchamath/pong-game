from turtle import Turtle
import random

MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.play_speed = 0.1
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.play_speed *= 0.9

    def reset_pos(self):
        self.goto((0, 0))
        self.bounce_x()
        self.play_speed = 0.1
