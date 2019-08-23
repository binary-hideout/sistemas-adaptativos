import math
import random
import pygame
from sys import argv

def explotar(pos_x, pos_y, radio, rgb_tuple):
    print("   Posición X:", pos_x)
    print("   Posición Y:", pos_y)
    print("   Radio:", radio)
    print("   Color en RGB:", rgb_tuple, "\n")

    screen = pygame.display.set_mode((800, 800))
    particles = [(random.gauss(0, 0.5), random.uniform(0, 6.28318)) for i in range(random.randint(50, 5000))]

    for i in range(radio):
        screen.fill((0, 0, 0))
        for speed, angle in particles:
            distance = i * speed
            x = pos_x + distance * math.cos(angle)
            y = pos_y + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), rgb_tuple)
        pygame.display.flip()

def secuencia_explosiones(cantidad, tipo = "diagonal", rgb_list = list()):
    """Genera la 'cantidad' de explosiones en el patrón especificado por 'tipo'.
    """
    # si la lista de colores está vacía
    if len(rgb_list) == 0:
        rgb_list = generarListaRGB(cantidad)

    step_x = 700 / cantidad
    step_y = step_x
    if tipo == "horizontal":
        pos_x = step_x
        pos_y = 400
        step_y = 0
    elif tipo == "vertical":
        pos_x = 400
        step_x = 0
        pos_y = step_y
    elif tipo == "diagonal":
        step_x = math.sqrt(2 * 400 * 400) / cantidad
        step_y = step_x
        pos_x, pos_y = step_x, step_y

    for i in range(cantidad):
        print(i + 1, "° explosión", sep='')
        radio = random.randint(200, 600)
        explotar(pos_x, pos_y, radio, rgb_list[i])

        pos_x += step_x
        pos_y += step_y

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

pygame.init()

print("3 llamadas a la función 'explotar'")
explotar(255, 500, 333, (0, 0, 255))
explotar(500, 100, 880, (0, 255, 0))
explotar(300, 221, 670, (255, 0, 0))

# validar si el comando contiene el argumento para la cantidad de explosiones
try:
    arg_ciclos = int(argv[1])
except:
    arg_ciclos = 2

# validar comando de tipo de patrón
try:
    arg_tipo = argv[2]
except:
    arg_tipo = "diagonal"

print("Llamada a la función 'secuencia_explosiones'")
secuencia_explosiones(arg_ciclos, arg_tipo.lower())