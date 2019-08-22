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
        screen.fill((0, 0, 0))
        for speed, angle in particles:
            distance = i * speed
            x = pos_x + distance * math.cos(angle)
            y = pos_y + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), rgb_tuple)
        pygame.display.flip()

def secuencia_explosiones(n, rgb_list):
    """Genera 'n' explosiones en un patrón de diagonal.
    """
    # si la lista de colores está vacía
    if len(rgb_list) == 0:
        rgb_list = generarListaRGB(n)

    # coordenadas del centro de la explosión
    pos_x, pos_y = 100, 100
    # incremento de las coordenadas para formar una diagonal
    step = math.sqrt(2 * 400 * 400) / n
    # contador
    for i in range(n):
        radio = random.randint(100, 700)
        
        print(i + 1, "° explosión", sep='')
        explotar(pos_x, pos_y, radio, rgb_list[i])

        pos_x += step
        pos_y = pos_x

def generarListaRGB(size):
    '''Genera una lista de tuples. Cada tuple contiene un color aleatorio en formato RGB.
    '''
    rgb_list = list()
    while size > 0:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        rgb = (red, green, blue)
        rgb_list.append(rgb)

        size -= 1

    return rgb_list

explotar(255, 500, 333, (0, 0, 255))
explotar(500, 100, 880, (0, 255, 0))
explotar(300, 221, 670, (255, 0, 0))

# validar si el comando contiene el argumento para la cantidad de explosiones
try:
    arg_ciclos = int(argv[1])
except:
    arg_ciclos = 2

rgb_list = generarListaRGB(arg_ciclos)
secuencia_explosiones(arg_ciclos, rgb_list)