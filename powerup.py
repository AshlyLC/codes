import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.image.load(f'{type}_powerup.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = type

    def update(self):
        pass  # Lógica de actualización para los potenciadores

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

def handle_powerup_collision(player, powerup):
    if player.rect.colliderect(powerup.rect):
        if powerup.type == 'speed':
            player.speed += 2
        elif powerup.type == 'invulnerable':
            player.invulnerable_time = 300  # Tiempo de invulnerabilidad
        elif powerup.type == 'disable':
            # Lógica para desactivar disparos del jefe por 6 segundos
            pass
        powerup.kill()
