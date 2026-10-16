años = []
info = []
estado = "cero"
        
def final():
    
    def identificar ():
        
        biciesto = False
    
        if año % 400 == 0:
            biciesto = True
        elif año % 100 == 0:
            biciesto = False
        elif año % 4 == 0:
            biciesto = True
        else:
            biciesto = False
            
        return biciesto
    
    for i in range(4):
        
        año = int(input("Seleccione su año:"))
        años.insert (0, año)
        identificar()
        if identificar()==True:
            estado = "biciesto"
        elif identificar()==False:
            estado = "normal"
        info.insert (0, estado)

        
final()
print (años)
print (info)
    
    
    
