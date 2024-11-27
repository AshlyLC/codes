numero = int(input("Escribe un número entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("¡DJ, pon la música de los 90s!")
elif numero % 3 == 0:
    print("¡DJ, pon la música de los 80s!")
elif numero % 5 == 0:
    print("¡DJ, pon la música electrónica!")
else:
    print("¡DJ, pon la música de moda!")