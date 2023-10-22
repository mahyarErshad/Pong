from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(x_position=350)
left_paddle = Paddle(x_position=-350)


screen.listen()
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()