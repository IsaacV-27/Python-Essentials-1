bloques = int(input("Ingresa el número de bloques: "))
altura = 0
var = bloques
for i in range(bloques):
    if (var > altura):
        altura += 1
        var -= altura  
        
print ("altura:", altura)

if var != 0:
    print ("La piramide esta incompleta")
