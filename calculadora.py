from tkinter import *
from math import *
from tkinter import ttk


#Probando hello world en tkinter
#############################################################################################
# root=Tk()
# ttk.Button(root, text="hello world in tk").grid()
# root.mainloop()
#############################################################################################
#Calculadora
#Creo la ventana
wn=Tk()
#le doy las dimensiones
wn.geometry('400x400')
#usando una carta de colores de tkinter, que encontre en google, elijo el color
#https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
wn.config(bg='SlateBlue4')
#a resizable le entrego los parametros 0 o false, para que no se pueda redimensionar
wn.resizable(0,0)
#Le doy un titulo a la ventana
wn.title('Calculadora by scu')
#################################################################################################
#Variables
buttonColor="turquoise"
buttonWidth=5
buttonHeight=3
#inicio la variable operador vacia
operator=""
#Inicio la variable para el texto a mostrar en pantalla con StringVar, que es el string de la biblioteca tkinter
screenText = StringVar()
#########################################################################################################
#Creo funciones

#Funcion para limpiar pantalla
def clear():
    #utilizo la variable operator como global en todas las funciones
    global operator
    #Limpio la variable operador
    operator= ""
    #Muestro 0 en la pantalla para cuando se limpie
    screenText.set("0")

#Funcion para cuando se hace click en un boton, que recibe b como parametro b, seria el texto del boton
def click(b):
    global operator
    #a operator le agrego el texto que se ingreso
    operator += str(b)
    #Actualizo el texto en pantalla
    screenText.set(operator)

#Funcion para cuando se aprete el boton igual
def equal():
    global operator
    #Con try y except evaluo si lo ingresado es interpretable por pyhton como codigo con eval, de otra forma
    #mostrara un mensaje de error al entrar al bloque except (excepciones)
    try:
        r = str(eval(operator))
    except:
        r="ERROR"
    #actualizo el texto en pantalla y mi variable operator con el ultimo valor
    operator=r
    screenText.set(r)

######################################################################################################################################
#creo los botones, asignandolos a la ventana wn, con su texto respectivo, la fuente y sus propiedades, el color del boton
#el ancho, alto y mediante command que en este contexto especificara que accion realizar cuando ocurra un evento, en este caso click
#entonces inicio una funcion anonima que llamara a la funcion declarada despues de :, con .grid, le asigno la posicion en la ventana
#al boton indicando la fila, columna, numero de columnas a utilizar y padding, que en palabras simples es como el margen de cada boton

#boton limpiar

buttonCe = Button(wn, text="C", font=("arial",10,"bold"), background=buttonColor, width=40, height=buttonHeight, command=lambda:clear())
buttonCe.grid(row=1, column=0, columnspan=4, padx=2,pady=2)

#botones primera fila

button1 = Button(wn, text="1", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(1))
button1.grid(row=2,column=0,columnspan=1,pady=2,padx=2)
button2 = Button(wn, text="2", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(2))
button2.grid(row=2,column=1,columnspan=1,pady=2,padx=2)
button3 = Button(wn, text="3", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(3))
button3.grid(row=2, column=2, columnspan=1, padx=2, pady=2)

#botones segunda fila

button4 = Button(wn, text="4", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(4))
button4.grid(row=3, column=0, columnspan=1, padx=2, pady=2)
button5 = Button(wn, text="5", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(5))
button5.grid(row=3, column=1, columnspan=1, padx=2, pady=2)
button6 = Button(wn, text="6", font=("arial", 10, "bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(6))
button6.grid(row=3, column=2, columnspan=1, padx=2, pady=2)

#botones tercera fila

button7 = Button(wn, text="7", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(7))
button7.grid(row=4, column=0, columnspan=1, padx=2, pady=2)
button8 = Button(wn, text="8", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(8))
button8.grid(row=4, column=1, columnspan=1, padx=2, pady=2)
button9 = Button(wn, text="9", font=("arial", 10, "bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(9))
button9.grid(row=4, column=2, columnspan=1, padx=2, pady=2)

#botones cuarta fila

button0 = Button(wn, text="0", font=("arial", 10, "bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(0))
button0.grid(row=5, column=0,   columnspan=1, padx=2, pady=2)
buttonFloat = Button(wn, text=".", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click("."))
buttonFloat.grid(row=5, column=1, columnspan=1,padx=2,pady=2)
buttonEqual = Button(wn, text="=", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:equal())
buttonEqual.grid(row=5, column=2, columnspan=1,padx=2,pady=2)

#botones de operaciones

buttonAdd = Button(wn, text="+", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("+"))
buttonAdd.grid(row=2, column=3,   columnspan=1, padx=2, pady=2)
buttonSub = Button(wn, text="-", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("-"))
buttonSub.grid(row=3, column=3,   columnspan=1, padx=2, pady=2)
buttonMul = Button(wn, text="*", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("*"))
buttonMul.grid(row=4, column=3,   columnspan=1, padx=2, pady=2)
buttonDiv = Button(wn, text="/", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("/"))
buttonDiv.grid(row=5, column=3,   columnspan=1, padx=2, pady=2)

screen=Entry(wn, font=("arial",20,"bold"), width=20, borderwidth=5, background="gold", textvariable=screenText)
screen.grid(row=0, column=0, columnspan=4, pady=4, padx=4)

#Con mainloop inicio un bucle infinito que estara constantemente atento a los eventos que ocurran en la ventana
#se ejecuta hasta que se cierre la ventana entre otras tareas, tambien se encarga de la actualizacion constante de la
#interfaz
wn.mainloop()

