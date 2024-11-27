class ObraDeArte:
    def __init__(self, titulo, autor, tipo, ano):
        self.titulo = titulo
        self.autor = autor
        self.tipo = tipo
        self.ano = ano

    def mostrar(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Tipo: {self.tipo}, Año: {self.ano}'

diccionario_obras = {}
next_obras_id = 0

def agregar_obra(titulo, autor, tipo, ano):
    global next_obras_id
    obra = ObraDeArte(titulo, autor, tipo, ano)
    diccionario_obras[next_obras_id] = obra
    next_obras_id += 1
    print(f'Obra agregada con ID: {next_obras_id - 1}')

def mostrar_obras():
    if not diccionario_obras:
        print('No hay obras de arte disponibles.')
    for id_obra, obra in diccionario_obras.items():
        print(f'ID: {id_obra}, {obra.mostrar()}')

def buscar_obra(id_obra):
    obra = diccionario_obras.get(id_obra)
    if obra:
        print(obra.mostrar())
    else:
        print('ID de obra no encontrado')

if __name__ == "__main__":
    agregar_obra('La Gioconda', 'Leonardo da Vinci', 'pintura', 1503)
    agregar_obra('El Pensador', 'Auguste Rodin', 'escultura', 1902)
    
    print("\nMostrar todas las obras:")
    mostrar_obras()
    
    print("\nBuscar obra con ID 0:")
    buscar_obra(0)
    
    print("\nBuscar obra con ID 2:")
    buscar_obra(2)