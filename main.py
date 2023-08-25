import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()

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
    # Slow down animation
    time.sleep(ball.play_speed)

    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with a paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect paddle_r missing the ball
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    # Detect paddle_l missing the ball
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

    scoreboard.update_score()

screen.exitonclick()
