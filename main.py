from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pongi")
user_l = screen.textinput(title="Player 1", prompt="What is your name left player?")
user_r = screen.textinput(title="Player 2", prompt="What is your name left player?")
try:
    win_point = int(screen.textinput(title="Win", prompt="What would you like to be the winning point?"))
except:
    win_point = 3

screen.tracer(0)

scoreboard = Scoreboard(user_l, user_r, win_point)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if abs(ball.ycor()) > 280:
        ball.tbounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.rbounce()
    if ball.xcor() > 360:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reset()
        scoreboard.r_point()
    if scoreboard.l_score > win_point-1 or scoreboard.r_score > win_point-1:
        scoreboard.end_of_game()
        cont = screen.textinput(title="Another round", prompt="Would you like to continue?(yes)")
        if cont.upper() != "YES":
            game_on = False
        else:
            ball.goto(0, 0)
            ball.move_speed = 0.1
            scoreboard.clear()
            scoreboard.l_score = 0
            scoreboard.r_score = 0
            scoreboard.update()
            screen.listen()
            screen.onkey(r_paddle.go_up, "Up")
            screen.onkey(r_paddle.go_down, "Down")
            screen.onkey(l_paddle.go_up, "w")
            screen.onkey(l_paddle.go_down, "s")


screen.exitonclick()
