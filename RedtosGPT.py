nreto = 0
import random 
def reto1 ():
    
    n = 0
    
    print ("eligio el Reto 1, Este muestra si un numero es par o impar")
    n = int(input("seleccione su numero: "))
    if n % 2 == 0:
        print ("el numero seleccionado es par")
    elif n%2!=0:
        print ("el numero seleccionado es impar")
    

def reto2 ():

    n = 0
    
    print ("eligio el Reto 2, Este muestra un contador de números")
    n = int(input("seleccione su numero para contar del 1 a el numero elegido: "))
    for i in range (1, n+1):
        print (i)
    
def reto3 ():

    n = 0
    suma = 1
    
    print ("eligio el Reto 3, Este suma los numeros otorgados por usted, para detenerlo debera seleccionar 0")
    while suma != 0:
        suma = int(input ("Numero:")) 
        n += suma
    print (n)

def reto4():

    n=0
    
    print ("eligio el Reto 4, le muestra las tablas de multiplicar de un numero elegido por usted")
    n = int(input("eliga el numero del que quiere ver la tabla"))
    for i in range (1, 11):
        print (n, "x", i, "=", n*i)

def reto5():

    intentos = 0
    n=0
    nsecreto = random.randint(1, 100)
    
    print ("eligio el Reto 5, Este es mas interesante, dentro del codigo hay un numero secreto, tu tendras que adivinar cual es mientras yo te digo si es mayor o menor")
    while n != nsecreto:
        n = int(input("Elige sabiamente:" ))
        if intentos == 4:
            print ("¡FALLASTE!")
            break
        else:
            if n<nsecreto:
                intentos +=1
                print ("Muy bajo")
                print ("intentos", intentos, "/5") 
            elif n>nsecreto:
                intentos +=1
                print ("Muy alto")
                print ("intentos", intentos, "/5")
            elif n==nsecreto:
                print ("¡ADIVINASTE!")
                break

print ("""
Retos de GPT
1. Reto 1
2. Reto 2
3. Reto 3
4. Reto 4
5. Reto 5
6. Break
""")

while nreto != 6:

    nreto = int(input("Seleccione su reto usando los numeros del 1 al 5 o use el 6 para salir "))

    if nreto <= 0 or nreto >=7:
        print ("numero invalido, empieze de nuevo y recuerde elegir entre el 1 y el 5 o 6 para salir ")

    if nreto == 1:
        reto1()

    if nreto ==2:
        reto2()
        
    if nreto == 3:
        reto3()

    if nreto ==4:
        reto4()

    if nreto ==5:
        reto5()
        
    if nreto==6:
        print ("Has elegido salir, hasta la proxima")
        break
    
