productos = [
    {
        "sku": 1,
        "producto": "Coca Cola",
        "precio": 15
    },
    {
        "sku": 2,
        "producto": "Gansito",
        "precio": 20
    },
    {
        "sku": 3,
        "producto": "Paketaxo",
        "precio": 60
    },
]

def print_productos(productos):
    for producto in productos:
        print(f"#SKU: {producto['sku']} | Nombre: {producto['producto']} | Precio: ${producto['precio']}")

def mostrar_menu():
    for i in range(3):
        print("==============================================================================================")
    print("===========================Bienvenido a Abarrotes \"El Hybridge\"===============================")
    for i in range(3):
        print("==============================================================================================")
    print("\t\t Menú de opciones")
    print("1) Punto de venta")
    print("2) Mostrar productos")
    print("3) Agregar producto")
    print("4) Modificar producto")
    print("5) Eliminar producto")
    print("6) Salir")
    print("==============================================================================================")
    
opc = 0        
while opc != 6:
    mostrar_menu()
    opc = int(input("Opción: "))
    if opc == 2:
        print_productos(productos)
