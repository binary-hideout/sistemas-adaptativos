from practica3.constantes import pesos, feromonas
from random import randint, random

def aco(pesos, feromonas, tasa_evaporacion, deposito):
    ciudad_actual = randint(0, 6)
    aptitudes = [(f / p) for f, p in zip(feromonas[ciudad_actual], pesos[ciudad_actual]) if p != 0]
    total = sum(aptitudes)
    probabilidades = [(a / total) for a in aptitudes]

    num_aleatorio = random()
    siguiente_ciudad = -1
    suma = 0
    for ciudad, probabilidad in enumerate(probabilidades):
        suma += probabilidad
        if num_aleatorio < suma:
            siguiente_ciudad = ciudad
            break

    