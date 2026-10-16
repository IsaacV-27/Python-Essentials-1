hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

sumamin = int(dura+mins)
horasalida= int(sumamin/60 + hour)
minsalida=int(sumamin%60)

if horasalida > 24:
   horasalida -= 24

print("la hora a la que finaliza el evento es:",horasalida,":",minsalida)
