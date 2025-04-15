agenda = {}

while(True):
    print("1. Añadir")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Salir")
    opcionMenu = input("Digite una opcion del menu: ")
    if opcionMenu == "1":
        #pedir datos
        nombre = input("Ingrese el nombre: ")
        if nombre in agenda:
            print("El nombre ya existe, y tiene asociado el telefono:", agenda[nombre])
            opcion = input("pulsa s si quiere modificar el telefono")
            if opcion == "s":
                telefono = input("Digite el telefono nuevo: ")
                agenda[nombre] = telefono
        else:
            telefono = input("digite el telefono: ")
            if telefono in agenda.values():
                print("el telefono ya existe")
            else:
                agenda[nombre] = telefono  
                print("agregadox") 
    elif opcionMenu == "2": 
        for clave,valor in agenda.items():
            print(clave ,"->",valor)
    elif opcionMenu == "3": 
        cadena = input("digite el nombre que desea buscar: ")
        for clave,valor in agenda.items():
            if clave.startswith(cadena):
                print(clave ,"->",valor)
    elif opcionMenu == "4":
        break
    else:
        print("digite una opcion correcta")    
  

