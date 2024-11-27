import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)
POWER_UP_INTERVAL = 5000  #5 seg

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Nave Espacial')

def load_and_scale_image(filename, size):
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, size)

background_image = load_and_scale_image('fondo.png', (SCREEN_WIDTH, SCREEN_HEIGHT))
ship_image = load_and_scale_image('nave.png', (90, 70))
ship_invincible_image = load_and_scale_image('nave2.png', (90, 70))
enemy_image = load_and_scale_image('pulpo.png', (400, 400))
enemy_image_hurt = load_and_scale_image('pulpo2.png', (400, 400))
bullet_image = load_and_scale_image('bala.png', (30, 30))
enemy_bullet_image = load_and_scale_image('agua.png', (30, 30))
explosion_image = load_and_scale_image('explosion.png', (100, 100))
gameover_image = load_and_scale_image('gameover.png', (400, 200))
victory_image = load_and_scale_image('victoria.png', (400, 200))
speed_power_up_image = load_and_scale_image('velocidad.png', (50, 50))

#sonidos
pygame.mixer.music.load('musica_fondo.mp3') 
pygame.mixer.music.play(-1)
hit_sound = pygame.mixer.Sound('hit.mp3') 
shoot_sound = pygame.mixer.Sound('shoot.mp3')

class Character(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self._speed = speed
        self._health = 100

    def update(self):
        pass

    def _take_damage(self, amount):
        self._health -= amount
        if self._health <= 0:
            self.kill()

    def get_rect(self):
        return self.rect

    def get_image(self):
        return self.image

class Ship(Character):
    def __init__(self):
        super().__init__(ship_image, 10, SCREEN_HEIGHT // 2, 5)
        self._invincible = False
        self._invincible_time = 0
        self._lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self._speed
        if keys[pygame.K_d]:
            self.rect.x += self._speed
        if keys[pygame.K_w]:
            self.rect.y -= self._speed
        if keys[pygame.K_s]:
            self.rect.y += self._speed
        #bordes
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        if self._invincible:
            if pygame.time.get_ticks() - self._invincible_time > 2000: 
                self._invincible = False
                self.image = ship_image

    def become_invincible(self):
        self._invincible = True
        self._invincible_time = pygame.time.get_ticks()
        self.image = ship_invincible_image

    def lose_life(self):
        self._lives -= 1
        if self._lives <= 0:
            return True
        return False

    def get_lives(self):
        return self._lives

class Enemy(Character):
    def __init__(self):
        super().__init__(enemy_image, SCREEN_WIDTH - 400, SCREEN_HEIGHT - 400, 0)
        self._original_image = enemy_image
        self._damaged_image = enemy_image_hurt
        self._shoot_timer = pygame.time.get_ticks()
        self._bullet_speed = 3 
        self._bullet_directions = [0, 45, 90, 135, 180, 225, 270, 315] 

    def update(self):
        current_time = pygame.time.get_ticks()
        
        if hasattr(self, '_damaged_time') and current_time - self._damaged_time > 2000: 
            self.image = self._original_image
            del self._damaged_time
        
        if current_time - self._shoot_timer > 2000: 
            self._shoot()
            self._shoot_timer = current_time

    def _shoot(self):
        for angle in self._bullet_directions:
            radian = math.radians(angle)
            dx = math.cos(radian) * self._bullet_speed
            dy = math.sin(radian) * self._bullet_speed
            bullet = EnemyBullet(self.rect.centerx, self.rect.centery, dx, dy)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)

    def take_damage(self):
        super()._take_damage(1)
        self.image = self._damaged_image 
        self._damaged_time = pygame.time.get_ticks() 

    def increase_bullet_speed(self, amount):
        self._bullet_speed += amount

    def set_bullet_directions(self, directions):
        self._bullet_directions = directions

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect(center=(x, y))
        self._speed = 7

    def update(self):
        self.rect.x += self._speed 
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = enemy_bullet_image
        self.rect = self.image.get_rect(center=(x, y))
        self._dx = dx
        self._dy = dy

    def update(self):
        self.rect.x += self._dx
        self.rect.y += self._dy
        if (self.rect.left < 0 or self.rect.right > SCREEN_WIDTH or
            self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT):
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, image, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.type = type
        self._speed = 5

    def update(self):
        self.rect.y += self._speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
power_ups = pygame.sprite.Group()

ship = Ship()
all_sprites.add(ship)

enemy = Enemy() 
all_sprites.add(enemy)
enemies.add(enemy)

score = 0
level = 1
last_power_up_time = pygame.time.get_ticks()

def draw_ui():
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {ship.get_lives()}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))
    screen.blit(level_text, (10, 70))

running = True
game_over = False
victory = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot_sound.play()
                bullet = Bullet(ship.rect.centerx + ship.rect.width // 2, ship.rect.centery) 
                all_sprites.add(bullet)
                bullets.add(bullet)

    if not game_over and not victory:
        current_time = pygame.time.get_ticks()
        if current_time - last_power_up_time > POWER_UP_INTERVAL:
            x = random.randint(0, SCREEN_WIDTH - 50)
            y = -50
            power_up = PowerUp(x, y, speed_power_up_image, 'speed')
            all_sprites.add(power_up)
            power_ups.add(power_up)
            last_power_up_time = current_time

        all_sprites.update()

        if level == 1:
            hits = pygame.sprite.groupcollide(bullets, enemies, True, False)
            for enemy_group in hits.values():
                for hit in enemy_group:
                    if isinstance(hit, Enemy):
                        hit.take_damage()
                        score += 10 

            if score >= 350 and level == 1:
                level = 2
                score = 0 
                enemy.increase_bullet_speed(3)
                enemy.set_bullet_directions([0, 55, 105, 145, 195, 255, 290, 345]) 
                enemy.rect.x = SCREEN_WIDTH - 400
                enemy.rect.y = SCREEN_HEIGHT - 400
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

        elif level == 2:
            hits = pygame.sprite.groupcollide(bullets, enemies, True, False)
            for enemy_group in hits.values():
                for hit in enemy_group:
                    if isinstance(hit, Enemy):
                        hit.take_damage()
                        score += 10  

            if score >= 500 and level == 2:
                level = 3
                score = 0 
                enemy.increase_bullet_speed(5) 
                enemy.set_bullet_directions([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330])
                enemy.rect.x = SCREEN_WIDTH - 400
                enemy.rect.y = SCREEN_HEIGHT - 400
                enemy = Enemy() 
                all_sprites.add(enemy)
                enemies.add(enemy)

        elif level == 3:
            hits = pygame.sprite.groupcollide(bullets, enemies, True, False)
            for enemy_group in hits.values():
                for hit in enemy_group:
                    if isinstance(hit, Enemy):
                        hit.take_damage()
                        score += 10 

            if len(enemies) == 0:
                victory = True
                screen.blit(victory_image, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100))
                pygame.display.flip()
                pygame.time.wait(3000) 
                running = False

        if pygame.sprite.spritecollideany(ship, enemy_bullets):
            if not ship._invincible:
                ship.become_invincible()
                if ship.lose_life():
                    game_over = True
                    screen.blit(explosion_image, (ship.rect.centerx - explosion_image.get_width() // 2, ship.rect.centery - explosion_image.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.wait(1000) 
                    screen.blit(gameover_image, (SCREEN_WIDTH // 2 - gameover_image.get_width() // 2, SCREEN_HEIGHT // 2 - gameover_image.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.wait(1000) 
                hit_sound.play()

        if pygame.sprite.spritecollideany(ship, power_ups):
            for power_up in pygame.sprite.spritecollide(ship, power_ups, True):
                if power_up.type == 'speed':
                    bullet._speed = 20
                    pygame.time.set_timer(pygame.USEREVENT + 1, 5000) 

        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        draw_ui()
        pygame.display.flip()

        pygame.time.Clock().tick(FPS)

if game_over:
    screen.blit(gameover_image, (SCREEN_WIDTH // 2 - gameover_image.get_width() // 2, SCREEN_HEIGHT // 2 - gameover_image.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

pygame.quit()
