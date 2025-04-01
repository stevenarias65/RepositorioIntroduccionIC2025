
edad = int(input("digite la edad: "))

if edad >= 18 and edad < 40:
    print("Es un joven adulto")
elif edad >= 40 and edad < 65:
    print("adulto")
elif edad >= 65 and edad < 70:
    print("adulto mayor")
else:
    print("ciudadano de oro")