opcion_deseada = "0"

while opcion_deseada != "6":
    print("*************Menú de opciones***********")
    print("1. Saludar")
    print("2. Pedir edad")
    print("3. Sumar 2 números")
    print("4. Restar 2 números")
    print("5. Multiplicar 2 números")
    print("6. Salir")
    
    opcion_deseada = input("Opción: ")
    
    if int(opcion_deseada) > 6 or int(opcion_deseada) < 1:
        print("*** -> Opción inválida. Vuelve a intentar")
        continue
    
    if opcion_deseada == "6":
        print("***************************")
        print("Fin. Adiós.")
        print("***************************")
        break
    
    print("==========================")
    print("Ejecutando opción " + opcion_deseada)
    print("==========================")
    
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
        num1 = int(input("Introduzca un número: "))
        num2 = int(input("Introduzca un número: "))
        print("El resultado de", str(num1), "x",num2, "es", (num1 * num2))
    
    continuar = input("Deseas continuar? (s/n): ")
    while continuar not in ['s', 'n']:
        print("Opción inválida. Vuelve a intentar")
        continuar = input("Deseas continuar? (s/n): ")
    
    if continuar == 'n':
        print("***************************")
        print("Fin. Adiós.")
        print("***************************")
        break