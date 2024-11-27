print("Bienvenido")

edad = (int(input("Ingresa tu edad: ")))

if edad >= 18:
    print("Adelante, puede pagar")
    dinero = (int(input("El costo de la cerveza es de $25, ingrese el dinero: ")))
    
    if dinero == 25:
        print("Gracias, vuelva pronto")
        
    elif dinero <25:
        print(int(input("Favor de depositar el monto completo: ")))
        
    else:
        print("Espere un momento para recibir su cambio")
   
else:
    print("Lo siento, no podemos venderle cerveza a un menor de edad")

   