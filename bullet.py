import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bala.png')
        self.image = pygame.transform.scale(self.image, (20, 10))  # Ajustar tamaño de la bala
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > 800:  # Asumiendo que el ancho de la pantalla es 800
            self.kill()  # Eliminar la bala si sale de la pantalla
