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
N_PIXELS_PER_FRAME = 3

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 4 - Cargar activos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('ball.png')

# 5 - Inicializamos variables
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH) 
ballY = random.randrange(MAX_HEIGHT) 
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Bucle infinito
while True:
  # 7 - Comprobar y manejar eventos
  for event in pygame.event.get():
    # ¿Se hizo clic en el botón de cierre? Salir de pygame y terminar el programa
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  # 8 - Realizar acciones "por cuadro"
  if (ballX < 0) or (ballX >= MAX_WIDTH): 
    xSpeed = -xSpeed # dirección contraria X
  if (ballY < 0) or (ballY >= MAX_HEIGHT):
    ySpeed = -ySpeed  # dirección contraria Y
   
  # Actualiza la localización de la pelota, usando la velocidad en dos direcciones
  ballX = ballX + xSpeed 
  ballY = ballY + ySpeed

  # 9 - Limpiar la ventana
  window.fill(BLACK)
  # 10 - Dibujar todos los elementos de la ventana
  window.blit(ballImage, (ballX, ballY))
  # 11 - Actualizar la ventana
  pygame.display.update()
  # 12 - Reducir la velocidad un poco
  clock.tick(FRAMES_PER_SECOND)