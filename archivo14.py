paises = []

while True:
    pregunta = int(input(
        "\n¿Qué deseas realizar?:\n"
        "1. Ingresar un país en la lista\n"
        "2. Borrar un país de la lista\n"
        "3. Buscar un país en la lista\n"
        "4. Salir\n"
    ))

    if pregunta == 1:
        paisIngresado = input("Ingresa el país a la lista:\n").capitalize()
        if paisIngresado in paises:
            print("Ese país ya está en la lista.")
        else:
            paises.append(paisIngresado)
            print(f"País {paisIngresado} ingresado.\nLista actual: {paises}")

    elif pregunta == 2:
        paisEliminado = input("Ingresa el país a eliminar de la lista:\n").capitalize()
        if paisEliminado in paises:
            paises.remove(paisEliminado)
            print(f"País {paisEliminado} eliminado.\nLista actual: {paises}")
        else:
            print("El país que escribiste no se encuentra en la lista.")

    elif pregunta == 3:
        paisBuscar = input("Ingresa país a buscar:\n").capitalize()
        if paisBuscar in paises:
            print("País encontrado en la lista!!")
        else:
            print("País no encontrado!!!")
        print(f"Lista actual: {paises}")

    elif pregunta == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
