productos = [
    {
        "sku": 1,
        "nombre": "Coca Cola",
        "precio": 15
    },
    {
        "sku": 2,
        "nombre": "Gansito",
        "precio": 20
    },
    {
        "sku": 3,
        "nombre": "Paketaxo",
        "precio": 60
    },
]

def print_productos(productos):
    for producto in productos:
        print(f"SKU: {producto['sku']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']}")

def buscar_producto(sku):
    for producto in productos:
        if producto['sku'] == sku:
            return producto
    return None

print_productos(productos)

def calcular_total(carrito):
    total = 0
    for item in carrito:
        producto = buscar_producto(item['sku'])
        if producto:
            cantidad = item['cantidad']
            precio_unitario = producto['precio']
            total += cantidad * precio_unitario
    return total

carrito = []
while True:
    sku = int(input("\nIngrese el SKU del producto que desea agregar al carrito (0 para terminar): "))
    producto_encontrado = buscar_producto(sku)
    if sku == 0:
        break
    cantidad = int(input(f"Ingrese la cantidad que desea llevar de {producto_encontrado['nombre']}: "))
    carrito.append({"sku": sku, "cantidad": cantidad})

total_a_pagar = calcular_total(carrito)
print(f"El total a pagar es: ${total_a_pagar}")