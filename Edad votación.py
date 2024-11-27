print("Consultar tu edad para votar:")

nombre = str(input("Escribe tu nombre: "))

print("Bienvenid@ al sistema electrónico de votación " + str(nombre))

edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("¡Felicidades, puedes votar " + str(nombre) + "!")
else:
    print("Aún no tienes edad para votar " + str(nombre))
    