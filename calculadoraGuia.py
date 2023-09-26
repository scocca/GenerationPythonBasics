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
        #Si esta vacio llamo a la funcion crearArray() para llenar el array
        crearArray()
    #Si no esta vacio se ejecutara el siguiente bloque de codigo
    else:
        #Creo e inicializo la variable result para almacenar el resultado, esta vezs la inicio en 1, para que al
        #Multiplicar no me arroje error
        result=1
        #Con un ciclo for recorro el arreglo o lista
        for i in numbers:
            #Cada iteracion multiplicara el result por el va,lor contenido en el indice actual (representado por i)
            result*= i  
        #muestro el resultado por pantalla     
        print(result)

#Declaro una nueva funcion llamada isEven que recible como parametro num
def isEven(num):
    #Evaluo si el modulo del numero sobre 2 es 0
    if num%2==0:
        #Si se cumple la condicion muestro un mensaje por pantalla
        print("el numero {num} es par")
        #Retorno el boolean solicitado en la guia
        return True
    #Si no se cumple la condicion anterior ingreso al siguiente bloque de codigo
    else:
        #Muestro un mensaje por pantalla
        print("el numero {num} no es par")
        #Retorno el boolean solicitado por la guia
        return False
#Return saca el valor deseado de nuestra funcion al plano superior, de no hacer un return todos los valores que trabajamos en la funcion
#moriran al terminar la ejecucion de esta

#Creo una nueva funcion llamada isItAnInteger que recibe num como parametro
def isItAnInteger(num):
    #evaluo si el numero se puede transformar a tipo int (Integer) enetero en spanish
    if type(num)==int:
        #si se cumple la condicion muestro el mensaje por pantalla
        print("El numero ingresado es un entero")
        #hagio el return del boolean solicitado por la guia
        return True
    #si no se ejecuto el bloque anterior, entro en el siguiente bloque de codigo
    else:
        #muestro un mensaje por pantalla
        print("El numero ingresado no es un entero")
        #Retorno el boolean solicitado por la guia
        return False

#Muestro un mensaje de bienvenida a nuestra calculadora
print("Bienvenido a la calculadora mejorada")
#inicio un ciclo infinito en donde se ejecutara nuestro codigo
while True:
    #Muestro el menu e instrucciones por pantalla 
    print("Instrucciones: para usar las opciones 2 y 3 primero debe ejecutar la opcion 6 .- Crear lista de numeros ")
    print("Seleccione una opcion")
    print("1.- Calculadora")
    print("2.- Sumar multiples numeros")
    print("3.- Multiplicar multiples numeros")
    print("4.- Verificar si el numero es Par")
    print("5.- Verificar si el numero es Entero (Integer)")
    print("6.- Crear lista de numeros")
    print("7.- Salir")
    #Solicito una entrada al usuario
    option=input("Ingrese una opcion: ")

    #Mediante sentencias if verifico el valor que ingreso el usuario
    if option=="1":
        #llamo a la funcion
        basicCalculator()
    elif option=="2":
        #llamo a la funcion entregandole el arreglo numbers como parametro
        addMultipleNumbers(numbers)
    elif option=="3":
        #llamo a la funcion entregandole el arreglo numbers como parametro
        multiplyMultipleNumbers(numbers)
    elif option=="4":
        #muestro un mensaje por pantalla
        print("Verificar si el numero es par")
        #declaro e inicializo una variable solicitando una entrada al usuario
        n=int(input("ingrese el numero a verificar: "))
        #llamo a la funcion entregando la variable anteriormente declarada e inicializada a la funcion isEven
        isEven(n)
    elif option=="5":
        #muestro un mensaje por pantalla
        print("Verificar si el numero es un entero (Integer)")
        #Declaro e inicializo una variable solicitando una entrada al usuario
        n=input("Ingrese el numero a verficiar: ")
        #llamo a la funcion isItAnInteger entregandole la variable anteriormente declarada e inicializada como parametro
        isItAnInteger(n)
    elif option=="6":
        #llamo a la funcion crear Arrary
        crearArray()
    elif option=="7":
        #Termino el bucle infinito con break
        break
    else:
        print("No se ingreso una opcion valida")
    

