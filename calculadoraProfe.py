def operations():
    while True:
        operation=input("Ingrese la operacion que desea realizar: ")
    
        try:
            result=eval(operation)
            print(result)
        except:
            print("Su operacion no se pudo realizar")
    
        option=input("Si desea realizar otra operacion presione enter, de lo contrario ingrese 1: ")

        if option=='1':
            print("gracias por utilizar esta calculadora")
            break
        
def isEven():
    print("Verificaremos si su numero es par")
    number=input("Ingrese el numero a verificar: ")
    flag:bool
    if number%2==0:
        flag=True
        print("su numero es par")
        print(flag)
    else:
        flag= False
        print("Su numero es impar")
        print(flag)
            
    return flag

def isInteger():
    print("verificaremos si su numero es entero")
    number=input("Ingrese el valor a verificar: ")
    if type(number)== int:
        print("El valor ingresado es un Integer")
        return(True)
    else:
        print("El valor ingresado no es un integer")
        return(False)


print("bienvenido a la calculadora")
while True:
    print("Lista de opciones")
    print("1.- operaciones basicas (suma, resta, multiplicacion division")
    print("2.- Es par")
    print("3.- es Integer")
    print("si desea cerrar la aplicacion presione enter")
    option=input("Ingrese su eleccion: ")

    if option=='1':
        operations()
    elif option=='2':
        isEven()
    elif option=='3':
        isInteger()
    else:
        if not option:
            break 



