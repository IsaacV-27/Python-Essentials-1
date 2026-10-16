numero = int(input("Digame su numero: "))
pasos = 0

while numero != 1:
    
    if (numero % 2 == 0):
        print(numero)
        pasos += 1
        numero /= 2
        
    elif (numero % 2 != 0) :
        print (numero)
        pasos +=1
        numero = (3 * numero) +1

print ("Pasos: ", pasos)
