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