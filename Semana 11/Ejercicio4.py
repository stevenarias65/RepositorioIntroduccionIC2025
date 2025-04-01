while True:
    nombre = input("Digite su nombre o escriba salir para terminar: ")

    if nombre.lower() == "salir":
        break

    if nombre == "":
        print("nombre vacio intente de nuevo")
        continue

    print("Hola",nombre)
