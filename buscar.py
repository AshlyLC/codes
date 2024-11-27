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

def buscar_producto(sku):
    for producto in productos:
        if producto['sku'] == sku:
            return producto
    return None

busqueda = int(input("Elige el número de SKU: "))
elemento_localizado = buscar_producto(busqueda)
if elemento_localizado:
    print(f"Producto localizado con SKU {busqueda}: {elemento_localizado['nombre']}")
else:
    print(f"No se localizó ningún producto con SKU {busqueda}")