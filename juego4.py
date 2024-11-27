import pygame
from pygame.locals import *
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 200
STEP_SIZE = 50 

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load('ball.png')

ballX = 0
ballY = 0
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
direction = (STEP_SIZE, STEP_SIZE)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            ballRect.x += direction[0]
            ballRect.y += direction[1]
            
            if ballRect.right > WINDOW_WIDTH or ballRect.left < 0:
                direction = (-direction[0], direction[1])
            if ballRect.bottom > WINDOW_HEIGHT or ballRect.top < 0:
                direction = (direction[0], -direction[1])

    window.fill(BLACK)
    
    window.blit(ballImage, ballRect.topleft)
    
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)