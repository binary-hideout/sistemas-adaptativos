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
    particles = [(random.gauss(0, 10), random.uniform(0, 6.28318)) for i in range(random.randint(500, 9000))]

    for i in range(radio):
        screen.fill((0, 0, 0))
        for speed, angle in particles:
            distance = i * speed
            x = pos_x + distance * math.cos(angle)
            y = pos_y + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), rgb_tuple)
        pygame.display.flip()

def secuencia_explosiones(tipo, cantidad, rgb_list = list()):
    """Genera 'n' explosiones en un patrón de diagonal.
    """
    screen_divide = math.floor(800 / cantidad)
    # si la lista de colores está vacía
    if len(rgb_list) == 0:
        rgb_list = generarListaRGB(cantidad)

    if tipo.lower() == "horizontal":
        for i in range(cantidad):
            explotar(i * screen_divide, 500, 500, rgb_list[i])
    elif tipo.lower() == "vertical":
        for i in range(cantidad):
            explotar(500, i * screen_divide, 500, rgb_list[i])
    elif tipo.lower() == "diagonal":
        for i in range(cantidad):
            explotar(i * screen_divide, i * screen_divide, 500, rgb_list[i])
    elif tipo.lower() == "random":
        for i in range(cantidad):
            explotar(random.randint(0, 800), random.randint(0, 800), 500, rgb_list[i])

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

print("3 llamadas a la función 'explotar'")
explotar(255, 500, 333, (0, 0, 255))
explotar(500, 100, 880, (0, 255, 0))
explotar(300, 221, 670, (255, 0, 0))

# validar si el comando contiene el argumento para la cantidad de explosiones
try:
    arg_tipo = argv[1]
    arg_ciclos = int(argv[2])
except:
    arg_ciclos = 2

print("Llamada a la función 'secuencia_explosiones'")
secuencia_explosiones(arg_tipo, arg_ciclos)