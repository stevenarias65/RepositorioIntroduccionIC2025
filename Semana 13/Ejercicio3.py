#creamos la lista de personales
personajes = []

#funcion de creacion de la comunidad del anillo
def agregar_personaje(nombre,clase,raza):
    p = {
        "nombre" : nombre,
        "clase" : clase,
        "raza" : raza
    }
    personajes.append(p)
    print("Personaje creado")

def mostrar_personajes():
    print("La comunidad del anillo")
    for p in personajes:
        print("El nombre del persona es: ",p["nombre"],"la raza es: ",p["raza"],"la clase es: ",p["clase"])



#Uso del programa
agregar_personaje("Aragorn","Rey","humano")
agregar_personaje("Frodo","Portador del anillo","Hobbit")
agregar_personaje("Gandalf","Mago","Maia")
agregar_personaje("Gimli","Guerrero","Enano")

mostrar_personajes()
