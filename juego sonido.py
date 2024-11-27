import pygame
from pygame.locals import *
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100  
STEP_SIZE = 5  

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load('ball.png')
ballImage = pygame.transform.scale(ballImage, (BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)) 
bounceSound = pygame.mixer.Sound('boing.mp3')
pygame.mixer.music.load('piano.mp3')
pygame.mixer.music.set_volume(0.2) 
pygame.mixer.music.play(-1, 0.0)  

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
                bounceSound.play() 
            if ballRect.bottom > WINDOW_HEIGHT or ballRect.top < 0:
                direction = (direction[0], -direction[1])
                bounceSound.play() 

    ballRect.x += direction[0]
    ballRect.y += direction[1]

    if ballRect.right > WINDOW_WIDTH or ballRect.left < 0:
        direction = (-direction[0], direction[1])
        bounceSound.play()
    if ballRect.bottom > WINDOW_HEIGHT or ballRect.top < 0:
        direction = (direction[0], -direction[1])
        bounceSound.play()  

    window.fill(BLACK)

    window.blit(ballImage, ballRect.topleft)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
