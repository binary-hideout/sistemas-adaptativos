import math
import random
import pygame
pygame.init()

def explotar(pos_x, pos_y, radio):
    print("Posición X:", pos_x)
    print("Posición Y:", pos_y)
    print("Radio:", radio, "\n")

    screen = pygame.display.set_mode((800, 800))
    particles = [(random.gauss(0, 0.5), random.uniform(0, 6.28318)) for i in range(2000)]

    for i in range(radio):
        screen.fill((255,255,255))
        for speed, angle in particles:
            distance = i * speed
            x = pos_x + distance * math.cos(angle)
            y = pos_y + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (0,0,0))
        pygame.display.flip()

def secuencia_explosiones(ciclos):
    if ciclos > 0:
        explotar(400, 400, 400)
        secuencia_explosiones(ciclos - 1)

secuencia_explosiones(2)