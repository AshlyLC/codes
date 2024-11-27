import random

tesoros = ["Reliquias", "Coronas", "Espadas", "Cofres", "Mapas", "Oro"]

print("Tesoros disponibles:")
for cosas in tesoros:
    print(cosas)

búsqueda = int(input("¿Cuántos objetos deseas seleccionar en tu búsqueda?: "))

print("Tesoros seleccionados en tu aventura:")
for x in range(búsqueda):
    selección = random.choice(tesoros)
    print(selección)