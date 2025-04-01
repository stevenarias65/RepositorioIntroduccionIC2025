#Bucles
#While
#for

#una variable que permita salir del ciclo 

contador = 1

while contador <= 10:
    print("Hola", contador)
    contador = contador + 1

opcion = "si"

while opcion.upper() == "SI":
    print("hola")
    opcion = input("desea continuar? digite si o no: ")


while True: 
    print("digite 1 para continuar o 2 para salir")
    dato = input()
    if dato == "2":
        break
