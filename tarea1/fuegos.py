import math
import random
import pygame
from sys import argv

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
        pos_x = random.randint(100, 700)
        pos_y = random.randint(100, 700)
        radio = random.randint(100, 700)

        explotar(pos_x, pos_y, radio)
        secuencia_explosiones(ciclos - 1)

try:
    arg_ciclos = int(argv[1])
except:
    arg_ciclos = 3
secuencia_explosiones(arg_ciclos)