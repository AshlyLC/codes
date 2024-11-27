while True:
    print("*************Menú de opciones***********")
    print("1. Saludar")
    print("2. Pedir edad")
    print("3. Sumar 2 números")
    print("4. Restar 2 números")
    print("5. Salir")
    print("==========================")
    
    opcion_deseada = input("Dame la opción deseada: ")
    if opcion_deseada == "1":
        print("Hola!")
    elif opcion_deseada == "2":
        edad = input("¿Cuál es tu edad?: ")
        print("Tienes", edad, "años.")
    elif opcion_deseada == "3":
        num1 = int(input("Introduzca un número: "))
        num2 = int(input("Introduzca un número: "))
        print("El resultado de", str(num1), " + ",num2, "es", (num1 + num2))
    elif opcion_deseada == "4":
        num1 = int(input("Introduzca un número: "))
        num2 = int(input("Introduzca un número: "))
        print("El resultado de", str(num1), "-",num2, "es", (num1 - num2))
    elif opcion_deseada == "5":
        print("El usuario salió")
        break