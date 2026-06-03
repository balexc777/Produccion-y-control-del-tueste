
while True:
    try:
        intensidad = int(input("Seleccione la intensidad de la curva del tueste:\n 1-suave\n 2-medio\n 3-intensad\n opcion:"))
        if intensidad in [1, 2, 3]:
            break
        else:
            print("Error. Debe ingresar 1, 2 o 3.")

    except ValueError:
        print("Error: Debe ingresar un número.")
if intensidad == 1:
    temp_min = 180
    temp_max = 200
elif intensidad == 2:
    temp_min = 200
    temp_max = 220
else:
    temp_min = 220
    temp_max = 240                

while True:
    try:
        minutos = int(input("Ingrese cuántos minutos va a durar el lote: "))

        if minutos <= 0:
            print("Error: El número de minutos debe ser positivo.")
        else:
            break

    except ValueError:
        print("Error: Debe ingresar un número entero.")

for i in range(minutos):

    while True:
        try:
            temperatura = float(input(f"Ingrese la temperatura del minuto {i+1}: "))
            break

        except ValueError:
            print("Error: Debe ingresar un número.")

print("Las temperaturas se registraron con éxito.")

