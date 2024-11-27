import pygame
import random

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLANCO = (255, 255, 255)
FPS = 30

class ObjetoJuego(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)

# Clase para la nave del jugador
class Nave(ObjetoJuego):
    def __init__(self, x, y):
        super().__init__(x, y, 'nave.png')
        self.vida = 100

    def mover(self, direccion):
        if direccion == 'izquierda':
            self.rect.x -= 5
        elif direccion == 'derecha':
            self.rect.x += 5

    def recibir_dano(self, cantidad):
        self.vida -= cantidad

# Clase para los enemigos
class Enemigo(ObjetoJuego):
    def __init__(self, x, y):
        super().__init__(x, y, 'enemigo.png')
        self.vida = 50

    def recibir_dano(self, cantidad):
        self.vida -= cantidad

# Clase para potenciadores
class Potenciador(ObjetoJuego):
    def __init__(self, x, y):
        super().__init__(x, y, 'potenciador.png')

# Configuración de la ventana del juego
pantalla = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Aventura Espacial")
clock = pygame.time.Clock()

# Instancia de la nave
nave = Nave(300, 400)
todos_sprites = pygame.sprite.Group()
todos_sprites.add(nave)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualización de los objetos
    todos_sprites.update()

    # Dibujo de los objetos
    pantalla.fill(BLANCO)
    todos_sprites.draw(pantalla)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()