import turtle
import time
from random import randrange, choice

wn=turtle.Screen()
wn.title("Snake by scu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

cordy=randrange(-290,290)
cordx=randrange(-390,390)

while cordy==0:
    cordy=randrange(-290,290)

while cordx==0:
    cordx=randrange(-390,390)

playerScore=0

food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(cordx,cordy)

snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0,0)

snake.dx=0.1
snake.dy=0.0


while True:
    wn.update()
    snake.setx(snake.xcor() + snake.dx)
    snake.sety(snake.ycor() + snake.dy)