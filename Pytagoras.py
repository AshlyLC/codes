import pygame
import random
import math

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Triángulos")

clock = pygame.time.Clock()

triangles = []

def generate_triangle():
    hipotenusa = random.randint(100, 200)
    ca = random.randint(50, hipotenusa)
    cb = int(math.sqrt(hipotenusa**2 - ca**2))
    return hipotenusa, ca, cb

def draw_triangle(ca, cb, x, y):
    point1 = (x, y)
    point2 = (x + ca, y)
    point3 = (x, y + cb)
    pygame.draw.polygon(screen, RED, [point1, point2, point3])

def can_draw_triangle(x, y, ca, cb):
    for tx, ty, t_ca, t_cb in triangles:
        if x < tx + t_ca and x + ca > tx and y < ty + t_cb and y + cb > ty:
            return False
    return True

def main():
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for tx, ty, ca, cb in triangles:
            draw_triangle(ca, cb, tx, ty)

        hipotenusa, ca, cb = generate_triangle()
        print(f"La hipotenusa es: {hipotenusa}")
        player_input = input("Ingresa un cateto: ")

        try:
            player_cateto = int(player_input)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if player_cateto != ca and player_cateto != cb:
            print("El cateto no es válido, intenta de nuevo.")
            continue

        x = random.randint(0, WIDTH - ca)
        y = random.randint(0, HEIGHT - cb)

        if can_draw_triangle(x, y, ca, cb):
            triangles.append((x, y, ca, cb))
        else:
            print("No puedes dibujar este triángulo aquí. Perdiste.")
            break

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    