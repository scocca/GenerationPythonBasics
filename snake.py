import turtle
import time
from random import randrange, choice

wn=turtle.Screen()
wn.title("Snake by scu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

cordy=randrange(-280,280)
cordx=randrange(-380,380)

while cordy==0 and cordy%20!=0:
    cordy=randrange(-280,280)

while cordx==0 and cordx%20!=0:
    cordx=randrange(-380,380)

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
snake.direction = "stop"


size=[]
size.append(snake)

def mov():
    
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)
    
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
                
def setMovUp():
    global snake
    if snake.direction!="down":
       snake.direction="up"

def setMovDown():
    global snake
    if snake.direction!="up":
        snake.direction="down"

def setMovRight():
    global snake
    if snake.direction!="left":
        snake.direction="right"

def setMovLeft():
    global snake
    if snake.direction!="right":
        snake.direction="left"    

wn.listen()
wn.onkeypress(setMovUp,"Up")
wn.onkeypress(setMovDown,"Down")
wn.onkeypress(setMovRight,"Right")
wn.onkeypress(setMovLeft,"Left")
speed=0.05
gameOver=False
while gameOver==False:

    mov()
    wn.update()
    if len(size)>1:
        for i in range(1,totalSize):
            sx=snake.xcor()
            sy=snake.ycor()
            if size[i].xcor()==sx and size[i].ycor()==sy:
                gameOver=True
                break
          
    if (food.xcor()-10<=snake.xcor()<=food.xcor()+10 and
        food.ycor()-10<=snake.ycor()<=food.ycor()+10):
        x = snake.xcor()
        y = snake.ycor()
        newPart=turtle.Turtle()
        newPart.speed(0)
        newPart.shape("square")
        newPart.color("white")
        newPart.penup()
        newPart.goto(x,y)
        size.append(newPart)
        cordy=randrange(-280,280)
        cordx=randrange(-380,380)
        while cordy%20!=0:
                    cordy=randrange(-280,280)

        while cordx%20!=0:
                    cordx=randrange(-380,380)
        food.goto(cordx,cordy)
        if speed>0.05:
            speed=speed-0.05
     
        wn.update()

    totalSize=len(size)
   
    for i in range(totalSize - 1,0,-1):
        x = size[i - 1].xcor()
        y = size[i - 1].ycor()
        size[i].goto(x, y)
      
       

    if totalSize>=0:
        x=snake.xcor()
        y=snake.ycor()
        size[0].goto(x,y)

    time.sleep(speed)