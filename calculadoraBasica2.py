
while True:
    
    print("Seleccione Opcion")
    print("1.-suma")
    print("2.-resta")
    print("3.-multiplicacion")
    print("4.-division")
    print("5.-salir")
    option=input()
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("ingrese el segundo numero: "))

    if not num1 or not num2:
        print("Error no se ha ingresado un numero o ingreso un valor 0")
    else:
        if option == '1':  
            result=num1+num2  
            print(result)
        elif option == '2':
            result=num1-num2  
            print(result)
        elif option == '3':
            result=num1*num2  
            print(result)
        elif option == '4':
            result=num1/num2  
            print(result)
        elif option == '5':
            print("Adios")
            break
        