def calculator():
    print("bienvenido a la calculadora")
    while True:
        print("Lista de opciones")
        print("1.- operaciones basicas (suma, resta, multiplicacion division")
        print("2.- Es par")
        print("3.- es Integer")
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
        

        
        def operations():
            operation=''
            operator=''
            print("escoja la operacion que desea realizar")
            print("1.-suma")
            print("2.-resta")
            print("3.-multiplicacion")
            print("4.-division")
            option=input("ingrese su eleccion: ")
            numbers=[]

            while True:
                number=input("ingrese un numero: ")
                numbers.append(number)
                if not number:
                    break

            if not operator:
                print("No se ha ingresado un operador")
            else:
                if option == '1':
                    operator='+'
                elif option == '2':
                    operator='-'
                elif option == '3':
                    operator='*'
                elif option == '4':
                    operator='/'

            for i in number:
                if len(numbers)>len(numbers):
                    operation+=i+operator
                else:
                    operation+=i
            result=0
            try:
                result=eval(operation)
            except:
                print("no se pudo realizar su operacion")
        
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





calculator()         



