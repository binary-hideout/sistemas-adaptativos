# Funciones de membresía para intensidad de golpe
from membresias import Membresias

class IntensidadGolpe():
    def leve(self, x):
        c = 10
        d = 30
        return Membresias.trapezoidalR(x, c, d)

from math import sqrt

# fuerza, velocidad
jaime_lannister = [0.6, 0.8]
khal_drogo = [0.7, 0.7]
robert_baratheon = [0.9, 0.5]

def distancia2D(p1, p2):
    return sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)

# centroide
centroides = [[255, 0, 0],
            [0, 255, 0],
            [0, 0, 255]]
# muestra
color3 = [209, 236, 121]

def distancia3D(p1, p2):
    return sqrt((p2[2] - p1[2]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)

def menorDistancia(centroides, muestra):
    menor = 999.9
    for i in range(3):
        dist = distancia3D(muestra, centroides[i])
        if dist < menor:
            menor = dist
            color = i
    return color