print("INICIO DEL PROGRAMA")

while True:
    try:
        numero_lote = int(input("Ingrese el numero de lote a realizar: "))

        if numero_lote <= 0:
            raise ValueError()

        break

    except ValueError:
        print("Error: Debe ingresar un número valido.")

print("FIN DEL BUCLE")