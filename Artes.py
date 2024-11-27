class Artwork:
    def __init__(self, titulo, autor, ano, tecnica):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.tecnica = tecnica

    def mostrar_detalles(self):
        """Muestra los detalles de la obra de arte."""
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.ano}")
        print(f"Técnica: {self.tecnica}")

    def actualizar_ano(self, nuevo_ano):
        """Actualiza el año de la obra de arte."""
        self.ano = nuevo_ano
        print(f"Año actualizado a: {self.ano}")

    def cambiar_tecnica(self, nueva_tecnica):
        """Actualiza la técnica de la obra de arte."""
        self.tecnica = nueva_tecnica
        print(f"Técnica actualizada a: {self.tecnica}")

obra1 = Artwork("La noche estrellada", "Vincent van Gogh", 1889, "Óleo sobre lienzo")
obra1.mostrar_detalles()
obra1.actualizar_ano(1890)
obra1.cambiar_tecnica("Óleo sobre lienzo con texturas")