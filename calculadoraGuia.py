#Crear la variable numbers que sera un arreglo o lista vacia
numbers=[]

#creamos una funcion llamada basiCalculator que no recibe parametros
def basicCalculator():
    #Iniciamos un bucle infinito
    while True:
        #Mostramos un mensaje por pantalla
        print("Si desea salir no ingrese un valor y presione enter")
        #Solicitamos una entrada por parte del usuario
        operation=input("Ingrese la operacion matematica que desea realizar: ")
        #Verificamos si la entrada esta vacia
        if not operation:
            #Si la entrada esta vacia entramos en el condicional if
            #y causamos el fin del bucle infinito
            break
        #Si la entrada no esta vacia con try-except veremos si se puede ejecutar un bloque de codigo
        try:
            #Bloque de codigo a evaluar. Declaramos la variable result la cual tomara el valor de eval(operatior)
            #el metodo eval(operation), recibira un string o cadena de caracteres y evaluara si es ejecutable como codigo python
            result=eval(operation)
            #Si se pudo ejecutar mostraremos el resultado por pantalla
            print(result)
        #En caso de no poder poder ejecutar el bloque de codigo que se encuentra dentro de try, pasamos a except
        except:
            #mostramos un mensaje de error
            print("Error: su operacion no se pudo realizar")

#Dado que para algunas funciones necesitaremos un arreglo, modificaremos el arreglo que declaramos vacio al inicio
#mediante una funcion nueva llamada crearArray que no recibe parametros , ya que seran solicitados en la misma funcion
def crearArray():
    #con numbers.clear() limpiamos nuestro arreglo o lista en caso de que este tenga informacion almacenada
    numbers.clear()
    #inciamos un bucle infinito
    while True:
        #Solicitamos una entrada al usuario
        number=input("Ingrese un numero entero a agregar a su array")
        #mostramos por pantalla la opcion para terminar el bucle infinito
        print("Si no desea agregar mas numeros ingrese t")
        #Verificamos que la opcion no sea la de termino del bucle antes de comenzar la operacion para agregar el valor al arreglo o lista
        if number=="t":
            #Con break finalizamos el bucle infinito
            break
        #Con try-except veremos si el codigo se puede ejecutar
        try:
            #Si el valor ingresado por el usuario puede ser transformado a tipo int (Integer) se agrega al array
            numbers.append(int(number))
        #Si el bloque de codigo dentro de try no se puede ejecutar, ingresamos al bloque contenido dentro de except
        except:
            #Mostramos un mensaje de error por pantalla
            print("El valor ingresado no es numero")

#Creamos una nueva funcion llamada addMultipleNumbers y esta recibe como parametro el arreglo o lista que declaramos
# al inicio del codigo        
def addMultipleNumbers(numbers):
    #verificamos que la lista o arreglo contenga informacion, en caso de estar vacia ejecutara la funcion crearArray()
    if len(numbers)==0:
        #llamo a la funcion
        crearArray()
    #En caso de que el arreglo no este vacio, se ejecutara el siguiente bloque de codigo
    else:
        #creo e inicializo una variable donde almacenare el resultado de la suma
        result=0
        #Mediante un ciclo for recorremos el arreglo, mientras i tenga alguna posicion en el arreglo, si llega al final de este finaliza
        for i in numbers:
            #En cada iteracion del ciclo for adicionaremos a result, el valor de la posicion del indice
            result+=i
        #muestro el resultado por pantalla
        print(result)

#creo una nueva funcion llamada multiplyMultipleNumbers que recibe como parametro un arreglo
def multiplyMultipleNumbers(numbers):
    #Verificamos si el arreglo esta vacio
    if len(numbers)==0:
        #Si esta vacio llamo a la funcion crearArray() para 
        crearArray()
    else:
        result=1
        for i in numbers:
            result*= i   
        print(result)

def isEven(num):
    if num%2==0:
        print("el numero {num} es par")
        return True
    else:
        print("el numero {num} no es par")
        return False

def isItAnInteger(num):
    if type(num)==int:
        print("El numero ingresado es un entero")
        return True
    else:
        print("El numero ingresado no es un entero")
        return False

print("Bienvenido a la calculadora mejorada")
while True:
    print("Instrucciones: para usar las opciones 2 y 3 primero debe ejecutar la opcion 6 .- Crear lista de numeros ")
    print("Seleccione una opcion")
    print("1.- Calculadora")
    print("2.- Sumar multiples numeros")
    print("3.- Multiplicar multiples numeros")
    print("4.- Verificar si el numero es Par")
    print("5.- Verificar si el numero es Entero (Integer)")
    print("6.- Crear lista de numeros")
    print("7.- Salir")
    option=input("Ingrese una opcion: ")

    if option=="1":
        basicCalculator()
    elif option=="2":
        addMultipleNumbers(numbers)
    elif option=="3":
        multiplyMultipleNumbers(numbers)
    elif option=="4":
        print("Verificar si el numero es par")
        n=int(input("ingrese el numero a verificar: "))
        isEven(n)
    elif option=="5":
        print("Verificar si el numero es un entero (Integer)")
        n=input("Ingrese el numero a verficiar: ")
        isItAnInteger(n)
    elif option=="6":
        crearArray()
    elif option=="7":
        break
    

