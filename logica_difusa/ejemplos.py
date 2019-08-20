# Funciones de membresía para intensidad de golpe
from Membresias import Membresias

class IntensidadGolpe():
    def leve(self, x):
        c = 10
        d = 30
        return Membresias.trapezoidalR(x, c, d)