#Programacion del juego pong con programacion basica (Sin programacion orientada
#a objetos), destacar que para compilar necesitaremos el modulo tkinter que
#utiliza python para la interfaz grafica: para instalarlo en wsl seguir los
#siguientes comandos en la terminal
#1.- sudo apt update
#2.- sudo apt upgrade
#3.- sudo apt intall python3-tk

#Importo la libreria turtle, que sirve para dibujar figuras en programas que 
#repiten moviemientos simples
import turtle
import time
from random import randrange, choice
#Genero un numero aleatorio entre 1 y -1, y mediante una condicion if, me aseguro que no sea 0
#se usara para que la pelota parta hacia un lado al azar
rand=randrange(-1,1)
if rand==0:
     rand=1
#################################################################################
#Creo una ventana
wn=turtle.Screen()
#Le asigno un titulo a mostrar en la ventana
wn.title("Pong by scu")
#cambio el color de fondo (backgroundcolo con bgcomolor)
wn.bgcolor("black")
#Redimensiono la ventana con setup y sus parametros width (ancho) y heicht (alto)
wn.setup(width = 800, height = 600)
#wn.tracer nos ayudara con la animacion para que se vea mas fluida
wn.tracer(0)

##################################################################################
#Procedo a crear los objetos del juego

#Declaro variables para el puntaje de los jugadores

playerOneScore=0
playerTwoScore=0

##################################################################################
#Jugadores

#con turtle.Turtle solo creo la representacion grafica del jugador 1
playerOne=turtle.Turtle()
#Con speed(0) le indico que aparezca en pantalla de forma inmediata cuando se ejecute
playerOne.speed(0)
#con shape() le doy forma al grafico
playerOne.shape("square")
#con color() le doy un color a mi cuadrado
playerOne.color("white")
#con penup() evito que el objeto deje un rastro al moverse
playerOne.penup()
#con goto() le doy la posicion al cuadrado
playerOne.goto(-350,0)
#le dare la forma de rectangulo al cuadrado para que sea mi paleta de pong
#con stretch multiplico los 20px por default de mi cuadrado por la cantidad
#indicada en este caso5 por tanto seria 20*5=100px en el ancho
playerOne.shapesize(stretch_wid=5, stretch_len=1)

#con turtle.Turtle solo creo la representacion grafica del jugador2
playerTwo=turtle.Turtle()
#Con speed(0) le indico que aparezca en pantalla de forma inmediata cuando se ejecute
playerTwo.speed(0)
#con shape() le doy forma al grafico
playerTwo.shape("square")
#con color() le doy un color a mi cuadrado
playerTwo.color("white")
#con penup() evito que el objeto deje un rastro al moverse
playerTwo.penup()
#con goto() le doy la posicion al cuadrado
playerTwo.goto(350,0)
#le dare la forma de rectangulo al cuadrado para que sea mi paleta de pong
#con stretch multiplico los 20px por default de mi cuadrado por la cantidad
#indicada en este caso5 por tanto seria 20*5=100px en el ancho
playerTwo.shapesize(stretch_wid=5, stretch_len=1)

##################################################################################
#Pelota

#procedemos a crear la pelota de la misma forma que los dos jugadores
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
#separamos los ejes con dx que cambiara los ejes de forma separada, el 3 significa 
#que se movera cada 1 pixel, controla la velocidad de la pelota
ball.dx=0.5*rand
ball.dy=0.5*rand

#muestro los contadores de puntaj en pantalla
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
#Comenta hideturtle() y busca la diferencia, es muy minima "Pista: esta cerca de la red"
pen.hideturtle()
pen.goto(0,260)
#.write es muy similar a print() y se usa en la biblioteca turtle
pen.write("Jugador 1: w,s       Jugador2: flechas ", align ="center", font=("courier", 25, "normal"))

inst=turtle.Turtle()
inst.speed(0)
inst.color("white")
inst.penup()
inst.hideturtle()
inst.goto(0,0)
inst.write("Atentos el juego ya comieza", align ="center", font=("courier", 25, "normal"))
##################################################################################
#agrego la representacion de la malla de una mesa de ping pong

web=turtle.Turtle()
web.color("white")
web.goto (0,400)
web.goto(0,-400)

###################################################################################
#comienzo a hacer las funciones que le daran vida al juego, y me permitiran conectar
#al teclado para realizar las interacciones

#le doy el nombre a mi funcion, en este caso para que la paleta del jugador 1, suba
def playerOne_up():
    if playerOne.ycor()+50<291:
    #obtengo la coordenada Y, almacenandola en una variable
        y=playerOne.ycor()
    #le sumo 20px a la variable y para que se mueva 20px hacia arriba
        y += 20
    #actualizo la coordenada del jugador 1, con el valor de la variable y
        playerOne.sety(y)

#le doy el nombre a mi funcion, en este caso para que la paleta del jugador 1, baje
def playerOne_down():
    if playerOne.ycor()-50>-291:
    #obtengo la coordenada Y, almacenandola en una variable
        y=playerOne.ycor()
    #le resto 20px a la variable y para que se mueva 20px hacia arriba
        y -= 20
    #actualizo la coordenada del jugador 1, con el valor de la variable y
        playerOne.sety(y)

#le doy el nombre a mi funcion, en este caso para que la paleta del jugador 2, suba
def playerTwo_up():
    if playerTwo.ycor()+50<291:
    #obtengo la coordenada Y, almacenandola en una variable
        y=playerTwo.ycor()
    #le sumo 20px a la variable y para que se mueva 20px hacia arriba
        y += 20
    #actualizo la coordenada del jugador 2, con el valor de la variable y
        playerTwo.sety(y)

#le doy el nombre a mi funcion, en este caso para que la paleta del jugador 2, baje
def playerTwo_down():
    if playerTwo.ycor()-50>-291:
    #obtengo la coordenada Y, almacenandola en una variable
        y=playerTwo.ycor()
    #le resto 20px a la variable y para que se mueva 20px hacia arriba
        y -= 20
    #actualizo la coordenada del jugador 2, con el valor de la variable y
        playerTwo.sety(y)


#Conecto el teclado

#inicio un listener, la funcion explicada en palabras simples es que estara "escuchando"
#para cuando se realize cierta accion para ejecutar otra
wn.listen()
#ahora a nuestros listeners les asignaremos la accion que deban "escuchar", y la funcion que
#deben ejecutar con onkeypress(funcion, teclaAsignada)
wn.onkeypress(playerOne_up, "w")
wn.onkeypress(playerOne_down, "s")
wn.onkeypress(playerTwo_up, "Up")
wn.onkeypress(playerTwo_down, "Down")

###################################################################################   
wn.update()
time.sleep(4)
pen.clear()
inst.clear()
pen.write("Player One: {}        Player Two: {}".format(playerOneScore,playerTwoScore), align ="center", font=("courier", 25, "normal"))
#inicio un bucle que sera el principal donde se correra el juego
while playerOneScore<11 or playerTwoScore<11:

        wn.update()
        #asigno el cambio en los ejes dentro del bucle, con los 3px que definimos en
        #ball.dx y dy
        
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
###################################################################################################
#Sistema de colicion
###################################################################################################
#Borde superior e inferior
    #Agrego el sistema de colicion al borde superior
        if ball.ycor()>290:
        #multiplico por -1 para dejar los 3px en negativo y asi que baje
             ball.dy *= -1
    #Agrego el sistema de colicion al borde inferior
        if ball.ycor()<-290:
        #en el caso del borde inferior tambien multiplico por -1 para que se
        #transforme a positivo
            ball.dy *=-1


########################################################################################
#Bordes laterales
    #En el caso de los bordes laterales devuelvo la pelota al centro, ya que si llegase a tocarlos
    #seria un punto, e invierto el valor de x para que el siguiente saque sea para el lado contrario
        if ball.xcor()>390:
        #Reseteo todas las posiciones a cero
            ball.goto(0,0)
            playerOne.goto(-350,0)
            playerTwo.goto(350,0)
            ball.dx *=-1
            playerOneScore+=1
        #Pen.clear() me limpiara el marcador para evitar sobreescritura
            pen.clear()
        #Vuelvo a escribir el marcador con la puntuacion actualizada
            pen.write("Player One: {}        Player Two: {}".format(playerOneScore,playerTwoScore), align ="center", font=("courier", 25, "normal"))
            wn.update()
            #verifico si el jugador llego al puntaje ganador para finalizar la partida, muestro un mensaje
            #y espero 5 segundos para terminar el programa
            if playerOneScore==11:
                 inst.write("Jugador 1 gano", align ="center", font=("courier", 25, "normal"))
                 time.sleep(5)
                 break
            time.sleep(1)

        if ball.xcor()<-390:
            ball.goto(0,0)
            playerOne.goto(-350,0)
            playerTwo.goto(350,0)
            ball.dx *=-1
            playerTwoScore+=1
            pen.clear()
            pen.write("Player One: {}        Player Two: {}".format(playerOneScore,playerTwoScore), align ="center", font=("courier", 25, "normal"))
            wn.update()
            if playerTwoScore==11:
                 inst.write("Jugador 2 gano", align ="center", font=("courier", 25, "normal"))
                 time.sleep(5)
                 break
            time.sleep(1)
####################################################################################
#Coliciones de las paletas

#mediante una estructura if verifico que la pelota se encuente entre en la superficie de la paleta
#en las coordenadas x e y, de los respectivos jugadores, de cumplirse la condicion le cambio el 
#simbolo + o - para que la pelota salga en direccion contraria
        if ((ball.xcor()>340 and ball.xcor()<350) and 
            (ball.ycor()<playerTwo.ycor()+50 and ball.ycor()>playerTwo.ycor()-50)):
                ball.dx*=-1

        if ((ball.xcor()<-340 and ball.xcor()>-350) and 
            (ball.ycor()<playerOne.ycor()+50 and ball.ycor()>playerOne.ycor()-50)):
                ball.dx*=-1
