
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