# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

lista_nombres_cuentas = [] 
lista_saldos_cuentas = [] 
lista_contrasenias_cuentas = []

def nueva_cuenta(nombre, saldo, contrasenia):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  lista_nombres_cuentas.append(nombre) 
  lista_saldos_cuentas.append(saldo) 
  lista_contrasenias_cuentas.append(contrasenia)

def show(numero_de_cuenta):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  print('       Cuenta', numero_de_cuenta)
  print('       nombre', lista_nombres_cuentas[numero_de_cuenta])
  print('       saldo:', lista_saldos_cuentas[numero_de_cuenta])
  print('       contraseña:',lista_contrasenias_cuentas[numero_de_cuenta])
  print()

def obtener_saldo(numero_de_cuenta, contrasenia):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  if contrasenia != lista_contrasenias_cuentas[numero_de_cuenta]:
    print('Contraseña incorrecta')
    return None
  return lista_saldos_cuentas[numero_de_cuenta]

def deposito(numero_de_cuenta, cantidad_deposito, contrasenia):
    global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
    if cantidad_deposito < 0:
        print('No puedes depositar una cantidad negativa!')
        return None
    if contrasenia != lista_contrasenias_cuentas[numero_de_cuenta]:
        print('Contraseña incorrecta')
        return None
    lista_saldos_cuentas[numero_de_cuenta] += cantidad_deposito
    return lista_saldos_cuentas[numero_de_cuenta]

def retiro(numero_de_cuenta, cantidad_retiro, contrasenia):
    global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
    if cantidad_retiro < 0:
        print('No puedes retirar una cantidad negativa!')
        return None
    if contrasenia != lista_contrasenias_cuentas[numero_de_cuenta]:
        print('Contraseña incorrecta')
        return None
    if cantidad_retiro > lista_saldos_cuentas[numero_de_cuenta]:
        print('No tiene saldo suficiente')
        return None
    lista_saldos_cuentas[numero_de_cuenta] -= cantidad_retiro
    return lista_saldos_cuentas[numero_de_cuenta]

print("La cuenta de Joe es la cuenta numero:", len(lista_nombres_cuentas)) 
nueva_cuenta("Joe", 100, 'soup')
print("La cuenta de Mary es la cuenta numero:", len(lista_nombres_cuentas)) 
nueva_cuenta("Mary", 12345, 'nuts')

while True:
    print()
    print('Presiona b para obtener tu saldo')
    print('Presiona d para hacer un deposito')
    print('Presiona w para hacer un retiro')
    print('Presiona s para mostrar la cuenta')
    print('Presiona q para salir')
    print()

    action = input('¿Qué te gustaría hacer? ')
    action = action.lower() 
    print()

    if action == 'b':
        print('Obtener saldo:')
        user_numero_de_cuenta = int(input('Por favor ingresa tu número de cuenta: '))
        user_contrasenia = input('Por favor ingresa la contrasenia: ')
        saldo = obtener_saldo(user_numero_de_cuenta, user_contrasenia)
        if saldo is not None:
            print('Tu saldo es:', saldo)
    elif action == 'd':
        print('Deposito:')
        user_numero_de_cuenta = int(input('Por favor ingresa tu número de cuenta: '))
        cantidad_a_depositar = int(input('Por favor ingresa la cantidad a depositar: '))
        user_contrasenia = input('Por favor ingresa la contrasenia: ')
        nuevo_saldo = deposito(user_numero_de_cuenta, cantidad_a_depositar, user_contrasenia)
        if nuevo_saldo is not None:
            print('Tu nuevo saldo es:', nuevo_saldo)
    elif action == 'w':
        print('Retiro:')
        user_numero_de_cuenta = int(input('Por favor ingresa tu número de cuenta: '))
        cantidad_a_retirar = int(input('Por favor ingresa la cantidad a retirar: '))
        user_contrasenia = input('Por favor ingresa la contrasenia: ')
        nuevo_saldo = retiro(user_numero_de_cuenta, cantidad_a_retirar, user_contrasenia)
        if nuevo_saldo is not None:
            print('Tu nuevo saldo es:', nuevo_saldo)
    elif action == 's':
        user_numero_de_cuenta = int(input('Por favor ingresa tu número de cuenta: '))
        show(user_numero_de_cuenta)
    elif action == 'q':
        break

print('Bye')