numbers=[]

def basicCalculator():
    while True:
        print("Si desea salir no ingrese un valor y presione enter")
        operation=input("Ingrese la operacion matematica que desea realizar: ")
        if not operation:
            break
        try:
            result=eval(operation)
            print(result)
        except:
            print("Error: su operacion no se pudo realizar")

def crearArray():
    numbers.clear()
    while True:
        number=input("Ingrese un numero entero a agregar a su array")
        print("Si no desea agregar mas numeros ingrese t")
        if number=="t":
            print(numbers)
            break
        numbers.append(int(number))
        print(numbers)
        
def addMultipleNumbers(numbers):
    if len(numbers)==0:
        crearArray()
    else:
        result=0
        for i in numbers:
            result+=i
        print(result)

def multiplyMultipleNumbers(numbers):
    if len(numbers)==0:
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
    

