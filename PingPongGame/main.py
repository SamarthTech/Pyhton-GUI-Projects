from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

UP = 'Up'
DOWN = 'Down'
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)  # Maybe screensize works as well
screen.title("PONG")
mid_line = Turtle()
mid_line.hideturtle()
mid_line.up()
mid_line.setheading(270)
mid_line.goto(0, 300)
mid_line.pencolor("white")
for i in range(15):
    mid_line.down()
    mid_line.forward(20)
    mid_line.up()
    mid_line.forward(20)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(key=UP, fun=r_paddle.go_up)
screen.onkeypress(key=DOWN, fun=r_paddle.go_down)
screen.onkeypress(key='w', fun=l_paddle.go_up)
screen.onkeypress(key='s', fun=l_paddle.go_down)
game_is_on = True
flag = 0
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # ball.move(flag)
    # # My method
    # if ball.ycor() > 280:
    #     flag = 1
    # elif ball.ycor() < -280:
    #     flag = 0

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 and ball.x_move > 0:
        ball.paddle_hit()

    if ball.distance(l_paddle) < 55 and ball.xcor() < -320 and ball.x_move < 0:
        ball.paddle_hit()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
