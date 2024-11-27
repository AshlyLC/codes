import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 200
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Cargar activos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('ball.png')

# Inicializar variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# Bucle infinito
while True:
    # Comprobar y manejar eventos
    for event in pygame.event.get():
        # ¿Se hizo clic en el botón de cierre? Salir de pygame y terminar el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Verificar si el usuario hizo clic
        if event.type == pygame.MOUSEBUTTONUP:
            # Verificar si el clic fue dentro del rectángulo de la bola
            if ballRect.collidepoint(event.pos):
                # Elegir una nueva ubicación aleatoria
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect.topleft = (ballX, ballY)

    # Realizar acciones "por cuadro"
    # Limpiar la ventana
    window.fill(BLACK)
    
    # Dibujar todos los elementos de la ventana
    window.blit(ballImage, ballRect.topleft)
    
    # Actualizar la ventana
    pygame.display.update()
    
    # Reducir la velocidad un poco
    clock.tick(FRAMES_PER_SECOND)
