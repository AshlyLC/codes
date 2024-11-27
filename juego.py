# pygame demo 0 - window only
# 1 - Import packages
import pygame
from pygame.locals import *
import sys
# 2 - Definimos constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
# 3 - Iniciamos el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock = pygame.time.Clock()
  # 4 - Cargamos asssets: imagenes(s), sonido(s), etc.
  # 5 - Inicializamos variables
  # 6 - Loop por siempre
while True:
  # 7 - Verificar y manejar los eventos
  for event in pygame.event.get():
    # ¿Se hizo clic en el botón de cerrar? Salir de pygame y finalizar el programa
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # 8 - Realizar acciones "por cuadro"
    # 9 - Limpiar la ventana
    window.fill(BLACK)
    # 10 - Dibujar todos los elementos de la ventana
    # 11 - Actualizar la ventana
    pygame.display.update()
    # 12 - Ralentizar un poco las cosas
    clock.tick(FRAMES_PER_SECOND)
    ballImage = pygame.image.load('ball.png') # 10 - Dibujar todos los elementos de la ventana
    window.blit(ballImage, (100, 200))
    # 11 - Actualizar la ventana
    pygame.display.update()
    # 12 - Ralentizar un poco las cosas
    clock.tick(FRAMES_PER_SECOND) 