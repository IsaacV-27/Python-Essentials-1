def biciesto (año):

    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return None
    elif año % 4 == 0:
        return True
    else:
        return None

def diadelmes(año,mes):

    if mes <=0 or mes >=13:
        return None
    elif mes >=1 and mes <=7:
        if mes == 2 and biciesto(año) == True:
            return 29
        elif mes == 2:
            return 28
        elif mes %2 == 0:
            return 30
        else:
            return 31
    if mes >=8 and mes <=12:
        if mes %2 == 0:
            return 31
        else:
            return 30

def diadelaño(año,mes,dia):
    
    if mes <=0 or mes >=13 or año <=0:
        return None
    
    elif dia <=0 or dia > diadelmes(año,mes):
            return None
    else:
        for i in range (1, mes):
            dia += diadelmes(año,i)
        return dia


print(diadelaño(2024, 2, 29))
print(diadelaño(2024, 13, 1))
print(diadelaño(1900, 3, 1))
print(diadelaño(2023, 2, 29))
print(diadelaño(2000, 12, 30))
