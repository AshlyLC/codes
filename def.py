def mayor(edad):
    if edad >= 18:
        return True
    else:
        return False
    
edad = int(input("Escribe tu edad: "))
resultado = mayor(edad)
print(resultado)
