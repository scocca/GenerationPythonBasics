print("Bienvenido a FIZZ BUZZ, si el numero es divisible por 3 responda fizz, si el numero es divisible por 5 responda buzz, si es divisible por ambos fizzBuzz, si no cumple ninguna regla solo repita el numero ")
array=[]
#declaro un array vacio el cual usare para almacenar los numeros
print("Cuantas rondas desea jugar")
limit=input()
#Capturo el input del usuario
if not limit:
    #Verifico que el input no este vacio (Null Safety)
    print("No se ha ingresado un valor")
else:
    #Si no esta vacio procedo a llenar el arreglo con la cantidad de nondas que desea el usuario
    for num in range(1,int(limit)+1):
        array.append(num)
#Declaro e inicializo una variable en 0 para el puntaje        
score=0

for num in array:
    #Con un ciclo for recorro el arreglo
    print('numero es: ' + str(num))
    #Por cada iteracion ira mostrando el numero que se entrega
    answer=input('tu respuesta: ')
    if not answer:
        #Compruebo que el usuario ingrese un valor (Null Safety)
        print("No se ha ingresado un valor")
    else:
    #Capturo la respuesta del usuario en una variable
        if num%15==0 and answer.lower()=='fizzbuzz':
        #evaluo si el modulo del numero entre 15 es cero y la respuesta es 'fizzbuzz' con un and (y)
        #aplico funcion lower para dejar todas las letras de la palabra 
        # almacenada en la variable en minusculas y comparo 
            score=score+5
        #Si se cumple la condicion anterior sumo 5 al puntaje
            if num < limit:
            # mediante un if anidado evaluo si quedan rondas para mostrar el mensaje de siguiente
                print('Correcto vamos al siguiente!')  
            else:
            #Si no se cumple solo le doy la instruccion de pasar
                pass
        elif num%5==0 and answer.lower()=='buzz':
        #Se repiten las instrucciones de la sentencia anterior
            score=score+5
            if num < limit:
                print('correcto vamos al siguiente!')  
            else:
                pass
        elif num%3==0 and answer.lower()=='fizz':
        #Se repiten las instrucciones de la sentencia anterior
            score=score+5
            if num < limit:
                print('correcto vamos al siguiente!')  
            else:
                pass
        elif str(num)==answer and num%3!=0 and num%5!=0:
        #Compruebo que el numero ingresado es igual al entregado
        #mediante sentencia and (y) tambien evaluo que el modulo sea diferente de 0
        #con 3 y 5, en este caso no considere 15 ya que es multiplo de 5 por tanto
        #no seria necesario  STR() TRANSFORMA NUM A STRING PARA PODER COMPARAR
            score=score+5
            if num < int(limit):
                print('correcto vamos al siguiente!')  
            else:
                pass
        else:
        #En caso de que no se cumpla ninguna de las evaluaciones anteriores muestra el fin del juego
            print('Fallaste')

#Una vez finalizado el ciclo muestro el mensaje final con su puntaje
print("Tu puntaje es: "+ str(score))
print("Fin del juego")
print("SCU")