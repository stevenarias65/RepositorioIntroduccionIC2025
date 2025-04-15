miDiccionario = {
    "nombre" : "Ronald Arias Fallas",
    "edad" : 32,
    "cedula" : "11111111111",
    "cursos" : ["Mate", "ingles", "progra"],
    "pasatiempos" : {"vaciones": ["Jugar", "ver series"],
                     "En clases": ["Estudiar","Ver peliculas"]}
    }

##Para accesar a el se usan las parentesis cuadrados
print(miDiccionario["cursos"][2])
print(miDiccionario["pasatiempos"]["vaciones"][0])

print(miDiccionario.keys())
print(miDiccionario.values())

miDiccionario["nombre"] = "Steven Arias Fallas"

print(miDiccionario)

miDiccionario["altura"] = 180

print(miDiccionario)

for i in miDiccionario.keys():
    print("Estos imprimiendo: ", i)
print("----")
for i in miDiccionario.values():
    print("Estos imprimiendo: ", i)
    
print("----")
for clave,valor in miDiccionario.items():
    print(clave , "el valor es: ", valor)


