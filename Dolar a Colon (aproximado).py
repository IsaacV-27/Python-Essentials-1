dolar = 1
colon = 500
proceso = 0

while True:
    
    proceso = float(input("Para pasar colones a dolares, precione 1\nPara pasar Dolares a Colones, precione 2\nO precione 0 para salir"))
    
    if proceso ==  1:
        ColRes = float(input("cuantos colones tiene?"))
        colonadolar = ColRes / colon
        print("Los",ColRes, "que usted me dio, son", colonadolar, "Dolares Estadounidenses")
        
    elif proceso == 2:
        DolRes = float(input("cuantos dolares tiene?"))
        dolaracolon = DolRes * colon
        print("Los",DolRes, "que usted me dio, son", dolaracolon, "Colones costarricences")
        
    elif proceso >=3:
        print("Se ha equivocado, por favor ingrese 1 o 2 para elegir el proceso que desea hacer")

    elif proceso == 0:
        print("Fue un placer ayudarle, vualva pronto")
        break
