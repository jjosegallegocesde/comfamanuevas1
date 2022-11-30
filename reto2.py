mes = input("¿En qué mes estás? ")

if mes == "marzo" or mes == "abril" or mes == "mayo":
    print("Estás en primavera")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print("Estás en verano")
elif mes == "septiembre" or mes == "octubre" or mes == "noviembre":
    print("Estás en otoño")
elif mes == "diciembre" or mes == "enero" or mes == "febrero":
    print("Estás en invierno")
else:
    print("Vuelva a introducir el mes")