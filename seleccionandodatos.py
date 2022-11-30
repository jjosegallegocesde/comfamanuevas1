#ENTRADAS DEL PROBLEMA
niveldeagua= int(input ("digita el nivel de agua"))

#EVALUANDO CAMNINOS MULTIPLES (MAS DE 2)
if niveldeagua<=100:
    print("Bajo nivel de agua")
elif niveldeagua >100 and niveldeagua<400:
    print("Operacion optima")
elif niveldeagua >= 400:
    print("Peligro....")
else:
    print("nivel de agua no valido")
