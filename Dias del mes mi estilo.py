años=[]
meses=[]
dias=[]

print("A continuacion, usted nos brindara un año y un mes y nosotros le diremos\ncuantos dias tiene ese mes\nDe ingresarse un mes invalido el valor que aparezca sera de 999")

def todo():
    
    def identificar ():
    
        if año % 400 == 0:
            return True
        elif año % 100 == 0:
            return False
        elif año % 4 == 0:
            return True
        else:
            return False

    for i in range(4):

        año = int(input("Seleccione su año:"))
        años.insert (0, año)
        mes = int(input("Seleccione su mes: "))
        meses.insert (0, mes)
        identificar()
        if mes <=0 or mes >=13:
            dia = 999
        elif mes >=1 and mes <=7:
            if mes == 2 and identificar() == True:
                dia = 29
            elif mes == 2:
                dia = 28
            elif mes %2 == 0:
                dia = 30
            else:
                dia = 31
        if mes >=8 and mes <=12:
            if mes %2 == 0:
                dia = 31
            else:
                dia = 30
        dias.insert (0, dia)
        
todo()
print (años)
print(meses)
print(dias)

