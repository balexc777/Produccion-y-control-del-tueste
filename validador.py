def evaluar_temperatura(temperatura, temp_min, temp_max):
    if temperatura >= temp_min and temperatura <= temp_max:
        print("Dentro del rango de seguridad")
    else:
        print("Fuera del rango de seguridad")


while True:
    try:
        Numero_lote = int(input("Ingrese el numero de lote a realizar:"))
        if Numero_lote <= 0:
            print("Debe ingresar un numero mayor a 0")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número.")

while True:
    try:
        intensidad = int(input("Seleccione la intensidad de la curva del tueste:\n 1-suave\n 2-medio\n 3-intensa\n opcion: "))
        if intensidad in [1, 2, 3]:
            if intensidad == 1:
                temp_min = 180
                temp_max = 200
            elif intensidad == 2:
                temp_min = 200
                temp_max = 220
            else:
                temp_min = 220
                temp_max = 240
            break
        else:
            print("Error. Debe ingresar 1, 2 o 3.")

    except ValueError:
        print("Error: Debe ingresar un número.")

while True:
    try:
        minutos = int(input("Ingrese cuántos minutos va a durar el lote: "))

        if minutos <= 0 or minutos > 60:
            raise ValueError()
        break

    except ValueError:
        print("Error: Debe ingresar un número valido.")

temperaturas = []

for i in range(minutos):
    while True:
        try:
            temperatura = float(input(f"Ingrese la temperatura del minuto {i+1}: "))
            if temperatura < 0 or temperatura > 500:
                raise ValueError()
            break

        except ValueError:
            print("Error: Debe ingresar un número valido.")

    temperaturas.append(temperatura)

print("Las temperaturas registradas son:")

for item in temperaturas:
    print(f"{item}°C")
    evaluar_temperatura(item, temp_min, temp_max)

print("Las temperaturas se registraron con éxito.")

print("---------------------")
print("- Resumen del lote  -")
print("---------------------")

print(f"Numero del lote: {Numero_lote}")
print(f"Duracion del lote: {minutos} minutos")

if intensidad == 1:
    print("Intensidad del lote: Suave")
elif intensidad == 2:
    print("Intensidad del lote: Media")
else:
    print("Intensidad del lote: Intensa")

print("Temperatura maxima:")
print("Temperatura media:")
print("Temperatura minima:")