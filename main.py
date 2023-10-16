from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def move_down():
    xcor = paddle.xcor()
    ycor = paddle.ycor() - 20
    paddle.goto(xcor, ycor)


def move_up():
    xcor = paddle.xcor()
    ycor = paddle.ycor() + 20
    paddle.goto(xcor, ycor)


screen.listen()
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_up, "Up")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()