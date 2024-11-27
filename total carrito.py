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
        print(f"#SKU: {producto['sku']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']}")

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
            numero = item['numero']
            precio_pz = producto['precio']
            total += numero * precio_pz
    return total

carrito = []
while True:
    sku = int(input("\nSeleccione el SKU del producto para agregar al carrito (0 para finalizar): "))
    elemento_localizado = buscar_producto(sku)
    if sku == 0:
        break
    numero = int(input(f"Elija la cantidad de {elemento_localizado['nombre']}: "))
    carrito.append({"sku": sku, "numero": numero})

pago_final = calcular_total(carrito)
print(f"El pago final es de: ${pago_final}")