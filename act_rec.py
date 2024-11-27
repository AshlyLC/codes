import pygame
import sys
from pygame.locals import *
from Rectangulo import *

# Definimos las constantes
BLANCO = (255,255,255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CUADROS_POR_SEGUNDO = 30
N_RECTANGULOS = 10
PRIMER_RECTANGULO = 'primer'
SEGUNDO_RECTANGULO = 'segundo'

# Preparamos la ventana
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

listaRectangulos = []
for i in range (0, N_RECTANGULOS):
  oRectangulo = Rectangulo(window)
  listaRectangulos.append(oRectangulo)

cualRectangulo = PRIMER_RECTANGULO

# loop principal
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == MOUSEBUTTONDOWN:
      for oRectangulo in listaRectangulos:
        if oRectangulo.clickedInside(event.pos):
          print ('Presionaste en el ',cualRectangulo,'rectángulo.')
          if cualRectangulo == PRIMER_RECTANGULO:
            oPrimerRectangulo = oRectangulo
            cualRectangulo = SEGUNDO_RECTANGULO
          elif cualRectangulo == SEGUNDO_RECTANGULO:
            oSegundoRectangulo = oRectangulo

            # El usuario ya escogió sus dos rectángulos, comparémoslos
            if oPrimerRectangulo == oSegundoRectangulo:
              print ('Los rectángulos son del mismo tamaño.')
            elif oPrimerRectangulo < oSegundoRectangulo:
              print ('El primer rectángulo es más chico que el segundo rectángulo.')
            else: # si no son iguales ni es más chico el primero, entonces debe ser más grande
              print ('El primer rectángulo es más grande que el segundo rectángulo.')

  # limpiamos la ventana y dibujamos todos los rectángulos
  window.fill(BLANCO)
  for oRectangulo in listaRectangulos:
    oRectangulo.draw()

  pygame.display.update()
  clock.tick(CUADROS_POR_SEGUNDO)