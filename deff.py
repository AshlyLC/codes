def explorar_territorio(H1, H2, H3, H4):
   
    herramientas = [H1, H2, H3, H4]

    longitud_max = max(len(h) for h in herramientas)
    longitud_max_h = [h for h in herramientas if len(h) == longitud_max]
    
    terminación_s_h = [h for h in herramientas if h.endswith('s')]

    if len(longitud_max_h) == 1 and len(terminación_s_h) == 1:
        resultado = f"¡Felicidades! La herramienta {longitud_max_h[0]} te ha dado ventaja por su longitud y la herramienta {terminación_s_h[0]} te ha dado ventaja por terminar en 's'."
    elif len(longitud_max_h) == 1:
        resultado = f"¡Felicidades! La herramienta {longitud_max_h[0]} te ha dado ventaja por su longitud."
    elif len(terminación_s_h) == 1:
        resultado = f"¡Felicidades! La herramienta {terminación_s_h[0]} te ha dado ventaja por terminar en 's'."
    elif len(longitud_max_h) == 2:
        resultado = f"¡Felicidades! Las herramientas {' y '.join(longitud_max_h)} te han dado ventaja por su longitud." 
    else:
        no_h = [h for h in herramientas if h not in longitud_max_h and h not in terminación_s_h]
        resultado = f"Fracasó. Ninguna de las herramientas {', '.join(no_h)} otorgó ventaja."

    return resultado

H1 = input("Herramienta 1: ")
H2 = input("Herramienta 2: ")
H3 = input("Herramienta 3: ")
H4 = input("Herramienta 4: ")

resultado = explorar_territorio(H1, H2, H3, H4)
print(resultado)
