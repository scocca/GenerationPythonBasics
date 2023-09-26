#Importo las librerias que voy a utilizar, en este caso serian turtle para graficos basicos
#time para la velocidad del juego y timers, y random para generar numeros aleatorios

import turtle
import time
from random import randrange, choice
#genero mi ventana donde se ejecutara el juego
wn=turtle.Screen()
wn.title("Snake by scu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#genero la vista en la ventana del texto que mostrara el puntaje y el fin del juego
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Puntaje: 0", align ="center", font=("courier", 25, "normal"))

#inicializo las coordenadas en donde aparecera la comida
cordy=randrange(-280,180)
cordx=randrange(-380,380)
#compruebo que las coordenadas sean multiplos de 20
while cordy==0 and cordy%20!=0:
    cordy=randrange(-280,180)

while cordx==0 and cordx%20!=0:
    cordx=randrange(-380,380)

#Creo la comida para mostrarla en pantalla
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(cordx,cordy)
#creo la cabeza de la serpiente
snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0,0)
#Creo un parametro llamado direccion que usare para asignar el movimiento de la serpiente
snake.direction = "stop"

#creo un arreglo vacio, y le inserto la cabeza de la serpiente, el arreglo se usara
#para ir agregando las partes de la serpiente detras de la cabeza
size=[]
size.append(snake)
#creo una funcion para los movimientos de la serpiente, que sera de 20px por la velocidad que tenga el juego
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

#################################################################################################
#Creo funciones seters para setear el moviemiento de la serpiente                
def setMovUp():
    global snake
    if snake.direction!="down":
       #intente usar un temporizador con el tiempo de actualizacion del juego para evitar un bug, que
       #consiste en que si cambio la direccion en el eje y o x, y vuelvo al eje anterior la serpiente choca
       #en el mismo eje de inicio con su cuerpo
       time.sleep(speed)
       snake.direction="up"

def setMovDown():
    global snake
    if snake.direction!="up":
        time.sleep(speed)
        snake.direction="down"

def setMovRight():
    global snake
    if snake.direction!="left":
        time.sleep(speed)
        snake.direction="right"

def setMovLeft():
    global snake
    if snake.direction!="right":
        time.sleep(speed)
        snake.direction="left"    

#Inicio y declaro listeners para que activen el movimiento de la serpiente con las
#flechas del teclado
wn.listen()
wn.onkeypress(setMovUp,"Up")
wn.onkeypress(setMovDown,"Down")
wn.onkeypress(setMovRight,"Right")
wn.onkeypress(setMovLeft,"Left")

#Declaro la variable de velocidad del juego, y la condicion de termino del juego con un boolean
speed=0.05
gameOver=False
#inicializo el ciclo principal del juego
while gameOver==False:
    #hago el llamado a la funcion encargada de los movimientos de la serpiente
    mov()
    #actualizo la pantalla
    wn.update()
    #Sistema de colision de la serpiente con su cuerpo
    if len(size)>1:
        #con un ciclo for reviso las coordenadas del cuerpo de la serpiente, evitando extraer
        #las coordenadas de la cabeza de la serpiente
        for i in range(1,totalSize):
            sx=snake.xcor()
            sy=snake.ycor()
            #realizo la comparacion con un condicional if, si entra en el bloque de codigo
            #entonces hara el fin del juego y mostrara el puntaje con el mensaje fin del juego
            #ademas de cambiar el estadode gameOver a true
            if size[i].xcor()==sx and size[i].ycor()==sy:
                gameOver=True
                snake.color("red")
                pen.clear()
                pen.write("Puntaje: {} - FIN DEL JUEGO".format(score), align ="center", font=("courier", 25, "normal"))
                turtle.done()
                break
    #sistema de colision de la serpiente con la comida mediant un condicional if, se le
    # suman y restan pixeles a las coordenadas de la comida respectivamente, para ampliar la
    # zona de colision       
    if (food.xcor()-12<=snake.xcor()<=food.xcor()+12 and
        food.ycor()-12<=snake.ycor()<=food.ycor()+12):
        #Obtengo las coordenadas de la cabeza de la serpiente
        x = snake.xcor()
        y = snake.ycor()
        #creo una nueva parte para el cuerpo de la serpiente
        newPart=turtle.Turtle()
        newPart.speed(0)
        newPart.shape("square")
        newPart.color("white")
        newPart.penup()
        #envio la nueva parte a las coordenadas en donde estaba la cabeza de la serpiente
        newPart.goto(x,y)
        #agrego la nueva parte al arreglo del cuerpo de la serpiente
        size.append(newPart)
        #genero nuevas coordenadas para que aparezca otra comida
        cordy=randrange(-280,180)
        cordx=randrange(-380,380)
        #inicializo una variable en true para verificar si lsa nuevas coordenadas de la comida
        #estan siendo usada por alguna parte del cuerpo de la serpiente
        occupied=True
        #con un ciclo while inicio la comprobacion de en estado de true, para verificar
        #que la comida no aparezca sobre una parte de la serpiente
        while occupied:
             cordx = randrange(-380, 380)
             cordy = randrange(-280, 180)  
            # se generan las coordenadas si esta ocupado y se hace la comprobacion con any para retornar un
            #booleano true si se cunmple a condicion y con abs comparamos los valores absolutos de las coordenadas
             occupied = any(abs(turtle.ycor() - cordy) < 20 for turtle in size) or any(abs(turtle.xcor() - cordx) < 20 for turtle in size) 
        #limpio el mensaje del puntaje para actualizarlo
        pen.clear()
        #obtengo el puntaje que sera el largo del arreglo -1 ya que debo restar la cabeza de la serpiente
        score=len(size)-1
        #muestro el mensaje por pantalla
        pen.write("Puntaje: {}".format(score), align ="center", font=("courier", 25, "normal"))
        #mando la comida a las coordenadas que ya fueron comprobadas si estan vacias
        food.goto(cordx,cordy)
        #disminuyo el tiempo para que la velocidad aumente de forma progresiva
        if speed>0.05:
            speed=speed-0.05
     
        wn.update()
    #obtengo el largo del arreglo del cuerpo de la serpiente nuevamente ya que el anterior fue dentro
    #del condicional if
    totalSize=len(size)
    #conun ciclo for recorro el arreglo desde la ultima a  segunda posicion hasta la ultima para actualizar las coordenadas
    #de cada parte del cuerpo para que vallan siguiendo a la cabeza, simulando que se arrastra y asi mantengo
    #los puntos de "pivoteo" cuando hago que cambie de eje
    for i in range(totalSize - 1,0,-1):
        #se obtienen las coordenadas de cada indice del arreglo
        x = size[i - 1].xcor()
        y = size[i - 1].ycor()
        #Se actualizan sus coordenadas y se nevia a esa posicion
        size[i].goto(x, y)
    
    #######################################################################################################
    #Sistema de colision con bordes, si la serpiente llega a cualquiera de los bordes, entonces aparecera
    #en el borde contrario, ejemplo: colisiona con el borde superior, aparecera por el inferior.
    if snake.xcor()>390:
        snake.goto(-390, snake.ycor())

    if snake.xcor()<-390:
        snake.goto(390, snake.ycor())

    if snake.ycor()>180:
        snake.goto(snake.xcor(),-280)
    
    if snake.ycor()<-280:
        snake.goto(snake.xcor(), 180)

#Velocidad del juego
    time.sleep(speed)

##asdasdasdasdasdasdasdasd
###asdasdasdasdasdasdasdasd
##asdasdasdasdasdasdasdasdasdasdasd