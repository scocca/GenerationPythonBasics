# Ciclos for:
# 1 Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.
#Mediante un ciclo for recorro los numeros del 1 al 10 utilizando range(), al parametro
#del maximo le sumo 1 ya que range funciona hasta n-1
for n in range(1,10+1):
    print(str(n))
# 2 Imprime los números pares del 1 al 20 utilizando un bucle for y una sentencia if.
#Mediante un ciclo for recorro los numeros del 1 al 20 utilizando range(), al parametro
#del maximo le sumo 1 ya que range funciona hasta n-1
for n in range(1, 20+1):
    #Verifico que el modulo del numero entre 2 sea cero, si es asi lo imprimo
    if n%2==0:
        print(str(n))
    else:
    #Si no se cumple la condicion anterior solo avanzo
        pass
# 3 Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario utilizando un bucle for.
print('Ingrese el numero del que desea conocer la tabala de multiplicacion')
#capturo el numero ingresado en una variable y los tranformo a tipo int
num=int(input())
#Verifico que el usuario efectivamente ingreso un valor si no muestro mensaje de error
if not num:
    print("no se ha ingresado ningun valor")
else:
    #Solicito al usuario el numero limite de la tabla de multiplicacion
    print('ingrese hasta que numero desea conocer las multiplicaciones')
#capturo el numero ingresado en una variable y los tranformo a tipo int
limit=int(input())
#Verifico que el usuario efectivamente ingreso un valor si no muestro mensaje de error
if not limit:
    print("no se ha ingresado ningun valor")
else:
    #
    for n in range(1,limit+1):
        mult=num*n
        print(str(num)+'*'+str(n)+'='+ str(mult))

# 4 Dada una lista de números, calcula la suma de todos los elementos utilizando un bucle for.
array=[]
print('Ingrese hasta que numero desea realizar la suma')
#capturo el valor ingresado por el usuario y lo transformo a tipo int
num=int(input())
#Verifico que el usuario efectivamente ingreso un valor si no muestro mensaje de error
if not num:
    print("no se ha ingresado ningun valor")
else:
    #si se ingreso un valor continuo con la ejecion del codigo, y mediante un ciclo for agrego los numeros
    #a un array con range()+1 y append() para ingresar el valor al final del array
    for n in range(1,num+1):
        array.append(num)
    #terminada la ejecucion del ciclo for, creo la variable total para almacenar la suma, que realizo
    #mediante sum() que suma todos los valores dentro del array
    total=sum(array)
    print('el total de la suma es: ' + str(total) )


#Ciclo While
# Crea un programa que cuente hacia atrás desde 10 hasta 1 utilizando un bucle while.
#declaro un contador en 1
counter=1
#Inicio el ciclo con la condicion que se detenga al ser menor o igual 10
while counter <=10:
    #muestro el numero por pantalla
    print(str(counter))
    #Adiciono 1 al contador
    counter=counter+1

# Escribe un programa que sume números ingresados por el usuario hasta que se 
# ingrese un número negativo utilizando un bucle while.

print("ingrese el primer numero distinto de 0 a sumar")
#capturo el valor ingresado por el usuario y lo transformo a tipo int
num=int(input())
#Declaro e inicio variables
sum=0
num2=0
#Verifico que el usuario efectivamente ingreso un valor si no muestro mensaje de error
if not num:
    print("no se ha ingresado ningun valor")
else:
    #procedo a solicitar y capturar el segundo numero
    print("ingrese el segundo numero distinto de 0 sumar")
    num2=int(input())
    if not num2:
        #Verifico que se ingreso un valor
        print("No se ha ingresado un valor")
    #Verifico que el numereo sea positivo
    elif num2>0:
        #Realizo la primera suma
        sum=num+num2
        print("suma: " + str(sum))
         #Inicio el ciclo while
        while num2 >= 0:
            #Solicito y capturo el valor en una nueva variable
            print("ingrese el otro numero distinto a 0 paraa sumar")
            num2=int(input())
            if not num2:
              #Verifico que se ingreso el valor
              print("No se ha ingresado un valor")
            elif num2<0:
              #verifico que el valor no sea negativo
              print("se ingreso un numero negativo")
            else: 
                #si pasa las pruebas anteriores hago la suma y muestro el resultado
                sum=sum + num2
                print("total sumado: "+ str(sum))    
    elif num2<0:
        #Verifico que el segundo numero solicitado sea positivo
        print("Numero negativo, no se puede proceder")

# Implementa un juego de adivinanza en el que el usuario debe adivinar un número secreto.
# Utiliza un bucle while para permitir múltiples intentos.

#importo libreria para generar numeros aleatorios
from random import randrange, choice
#inicializo mi variable y le asigno un valor aleaatorio mediante randrange(limite inferior, limite superior)
rand=randrange(1,11)
print(str(rand))
#Solicito y almaceno el input del usuario
print("adivina el numero, ingresa un valor entre 1 y 10, tienes 3 intentos")
inp=int(input())
#inicio ciclo for, verificando que el valor ingresado por el usuario sea diferente al numero generado
counter=1
while inp!=rand:
    print("no has acertado")
    print("intentalo nuevamente")
    inp=int(input())
    counter=counter+1
    if counter==3 and inp!=rand:
        print("Perdiste")
        break
#muestro por pantalla el mensaje final
print("Felicidades has adivinado")

# Calcula el factorial de un número ingresado por el usuario utilizando un bucle while.
print("Ingresa un numero distinto de 0 para calcular su Factorial")
#Solicito el numero al usuario
num=int(input())
#Verifico que el usuario halla ingresado un valor
if not num:
    #Si no ingreso el valor, muestro mensaje de error
    print("No se ha ingresado un valor")
else:
  pass
#Inicializo variables
counter=num-1
fact=0
#Inicio ciclo for hasta que el contador sea 0
while counter>0:
  #Sumo el factorial
  fact=fact+(num*counter)
  #Le descuento 1 al contador
  counter=counter-1
  #Muestro el resultado
  print(str(fact))

# Crea un programa que genere la secuencia de Fibonacci hasta un número dado utilizando un bucle while.

print("Ingresa un numero distinto de 0 para calcular su secuencia de fibbonacci")
#Solicito el numero al usuario
num=int(input())
#Verifico que el usuario halla ingresado un valor
if not num and num!=1:
    #Si no ingreso el valor, muestro mensaje de error
    print("No se ha ingresado un valor o ingreso valor 1")
else:
  pass
#Inicializo variables
a=0
b=1
sum=1
count=1
#muestro por pantalla el encabezado del resultado
print("la secuencia de fibonaccci es: " + " ")
#Uso ciclo while
while(count<=num):
    #Adiciono al contador
    count+=1
    print(a, end=" ")
    a=sum
    sum=a+b

# Escribe un programa que determine si un número ingresado por el usuario es
#  positivo o cero utilizando sentencias if.

print("Ingrese un numero para verificar si es positivo")
num=int(input())

if not num:
    print("no se ha ingresado un numero")
elif num>0:
    print("El numero ingresado es positivo")
elif num==0:
    print("el numero ingresado es 0")
else:
    print("El numero ingresado es negativo")

# Crea un programa que verifique si un número es par o impar 
# utilizando una sentencia if.
print("Ingrese un numero para verificar si es par o impar")
num=int(input())

if not num:
    print("no se ha ingresado un numero")
elif num%2==0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

# Implementa un programa que determine si un año ingresado por el usuario
#  es bisiesto o no utilizando sentencias if.
print("Ingrese un annio para verificar si es positivo")
year=int(input())

if not year:
    print("no se ha ingresado un numero")
elif num%4==0:
    print("El annio es bisiesto")
else:
    print("El annio no es bisiesto")

# Solicita al usuario ingresar dos números y determina cuál de ellos 
# es mayor utilizando sentencias if.
print("Ingrese el primer numero para ver cual es mayor")
a=int(input())
print("Ingrese el segundo numero para ver cual es mayor")
b=int(input())

if not a or b:
    print("no se ha ingresado un numero")
elif a>b:
    print("El numero: " + str(a) +" es el mayor")
else:
    print("El numero: " + str(b) +" es el mayor")