while True:
    print("Bienvenido a la calculadora basica")
    num1=(input("Ingrese el primer numero: "))
    num2=(input("ingrese el segundo numero: "))
    num3=(input("Si lo desea ingrese un tercer numero, de lo contrario presione enter: "))
    operator=(input("ingrese la operacion que desea realizar: suma(+), resta(-), multiplicacion(*), division(/): "))
    result=0
    if not num1 or not num2:
        print("Error no se ha ingresado un numero o se ingreso un valor 0")
    else:
        if not num3:
            result=eval(num1+operator+num2)
        else:
            if not num3:
                print("No se ingreso el tercer valor o es 0")
            else:
                result=eval(num1+operator+num2+operator+num3)
    print("el resultado de su operacion es: " + str(result))
    exit=input("Si desea realizar otra operacion presione enter, si desea salir ingrese 2: ")
    
    if exit=='2':
        break