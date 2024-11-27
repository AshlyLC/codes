# pygame demo 2 - una imagen, clic y movimiento
# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys
import random
# 2 - Definir constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 200
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 4 - Cargar activos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('ball.png')
# 5 - Inicializar variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
# 6 - Bucle infinito
while True:
  # 7 - Comprobar y manejar eventos
  for event in pygame.event.get():
    # ¿Se hizo clic en el botón de cierre? Salir de pygame y terminar el programa
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # Verificar si el usuario hizo clic
    if event.type == pygame.MOUSEBUTTONUP:
    #mouseX, mouseY = event.pos  # Podría hacerse esto si lo necesitáramos
    # Verificar si el clic fue dentro del rectángulo de la bola
    # Si es así, elegir una nueva ubicación aleatoria
      if ballRect.collidepoint(event.pos):
        ballX = random.randrange(MAX_WIDTH)
        ballY = random.randrange(MAX_HEIGHT)
        ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
  # 8 - Realizar acciones "por cuadro"
  # 9 - Limpiar la ventana
  window.fill(BLACK)
  # 10 - Dibujar todos los elementos de la ventana
  # Dibujar la bola en la ubicación aleatoria
  window.blit(ballImage, (ballX, ballY))
  # 11 - Actualizar la ventana
  pygame.display.update()
  # 12 - Reducir la velocidad un poco
  clock.tick(FRAMES_PER_SECOND)