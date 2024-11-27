import pygame
from pygame.locals import *
import sys

BACKGROUND_COLOR = (183, 54, 250) 
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

emojiImage = pygame.image.load('emoji.png') 

emojiRect = emojiImage.get_rect()

emojiRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BACKGROUND_COLOR)

    window.blit(emojiImage, emojiRect.topleft)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)