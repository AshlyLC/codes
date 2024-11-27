import random

variable = random.randint(1, 100)

intentos = 0
while True:
    intento = int(input("Intenta adivinar el número que está entre el 1 al 100: "))
    intentos += 1

    if intento > variable:
        print("El número es menor")
    elif intento < variable:
        print("El número es mayor")
    else:
        print(f"¡Felicidades!¡Has adivinado el número secreto!")
        break