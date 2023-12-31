from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboad import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(x_position=350)
left_paddle = Paddle(x_position=-350)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_on = True

while game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        scoreboard.right_score()

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.left_score()

screen.exitonclick()