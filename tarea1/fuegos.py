import math
import random
import pygame
from sys import argv

pygame.init()

def explotar(pos_x, pos_y, radio, rgb_tuple):
    print("   Posición X:", pos_x)
    print("   Posición Y:", pos_y)
    print("   Radio:", radio)
    print("   Color en RGB:", rgb_tuple, "\n")

    screen = pygame.display.set_mode((800, 800))
    particles = [(random.gauss(0, 0.5), random.uniform(0, 6.28318)) for i in range(2000)]

    for i in range(radio):
        screen.fill((255,255,255))
        for speed, angle in particles:
            distance = i * speed
            x = pos_x + distance * math.cos(angle)
            y = pos_y + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), rgb_tuple)
        pygame.display.flip()

def secuencia_explosiones(ciclos, rgb_list):
    for i in range(ciclos):
        pos_x = random.randint(100, 700)
        pos_y = random.randint(100, 700)
        radio = random.randint(100, 700)

        print(i + 1, "° explosión", sep='')
        explotar(pos_x, pos_y, radio, rgb_list[i])

def generarListaRGB(size):
    '''Genera una lista de tuples. Cada tuple contiene un color aleatorio en formato RGB.
    '''
    rgb_list = list()
    for i in range(size):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        rgb = (red, green, blue)
        rgb_list.append(rgb)
    return rgb_list

# validar si el comando contiene el argumento para la cantidad de explosiones
try:
    arg_ciclos = int(argv[1])
except:
    arg_ciclos = 3

rgb_list = generarListaRGB(arg_ciclos)
secuencia_explosiones(arg_ciclos, rgb_list)