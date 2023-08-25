from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()

# Create screen
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")

# Stop auto-animations
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()

# Event listeners
screen.listen()
# Right paddle controls
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
# Left paddle controls
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

is_game_on = True
while is_game_on:
    # Run animations
    screen.update()
    ball.move()

screen.exitonclick()
