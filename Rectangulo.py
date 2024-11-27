import pygame
import random

class Rectangulo:
    def __init__(self, window):
        self.window = window
        self.width = random.randint(20, 100)
        self.height = random.randint(20, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rect = pygame.Rect(
            random.randint(0, window.get_width() - self.width),
            random.randint(0, window.get_height() - self.height),
            self.width,
            self.height
        )

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def clickedInside(self, pos):
        return self.rect.collidepoint(pos)

    def __lt__(self, other):
        return self.width * self.height < other.width * other.height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height