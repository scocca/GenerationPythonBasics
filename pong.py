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
#que se movera cada 3 pixeles
ball.dx=1
ball.dy=1

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
    #obtengo la coordenada Y, almacenandola en una variable
    y=playerOne.ycor()
    #le sumo 20px a la variable y para que se mueva 20px hacia arriba
    y += 20
    #actualizo la coordenada del jugador 1, con el valor de la variable y
    playerOne.sety(y)

#le doy el nombre a mi funcion, en este caso para que la paleta del jugador 1, baje
def playerOne_down():
    #obtengo la coordenada Y, almacenandola en una variable
    y=playerOne.ycor()
    #le resto 20px a la variable y para que se mueva 20px hacia arriba
    y -= 20
    #actualizo la coordenada del jugador 1, con el valor de la variable y
    playerOne.sety(y)

#le doy el nombre a mi funcion, en este caso para que la paleta del jugador 2, suba
def playerTwo_up():
    #obtengo la coordenada Y, almacenandola en una variable
    y=playerTwo.ycor()
    #le sumo 20px a la variable y para que se mueva 20px hacia arriba
    y += 20
    #actualizo la coordenada del jugador 2, con el valor de la variable y
    playerTwo.sety(y)

#le doy el nombre a mi funcion, en este caso para que la paleta del jugador 2, baje
def playerTwo_down():
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
#inicio un bucle que sera el principal donde se correra el juego

while True:
    wn.update()
    #asigno el cambio en los ejes dentro del bucle, con los 3px que definimos en
    #ball.dx y dy
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Agrego el sistema de colicion al borde superior
    if ball.ycor()>290:
        #multiplico por -1 para dejar los 3px en negativo y asi que baje
        ball.dy *= -1
    #Agrego el sistema de colicion al borde inferior
    if ball.ycor()<-290:
        #en el caso del borde inferior tambien multiplico por -1 para que se
        #transforme a positivo
        ball.dy *=-1


