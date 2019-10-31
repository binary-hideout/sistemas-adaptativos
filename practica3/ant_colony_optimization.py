from random import randint, random
from sys import float_info

def siguienteCiudad(probabilidades, ciudades_recorridas):
    '''Selecciona la siguiente ciudad.
    '''
    num_aleatorio = random()
    suma = 0
    for ciudad, probabilidad in enumerate(probabilidades):
        suma += probabilidad
        if ciudad not in ciudades_recorridas and num_aleatorio < suma:
            return ciudad

def seleccionarProbabilidades(pesos, feromonas):
    '''Calcula las probabilidades para cada ciudad a escoger.
    '''
    aptitudes = [(feromona / peso) if peso != 0 else 0 for peso, feromona in zip(pesos, feromonas)]
    total = sum(aptitudes)
    probabilidades = [(a / total) for a in aptitudes]

    return probabilidades

def recorrerGrafo(pesos, feromonas, ciudad_inicial):
    '''Hace un recorrido por el grafo.
    '''
    ciudades_recorridas = [ciudad_inicial]

    for _ in range(5):
        ciudad_actual = ciudades_recorridas[-1]

        # filtrar pesos y feromonas adyacentes a la ciudad actual
        pesos_adyacentes, feromonas_adyacentes = list(), list()
        for (ciudad, peso), feromona in zip(enumerate(pesos[ciudad_actual]), feromonas[ciudad_actual]):
            if ciudad in ciudades_recorridas:
                pesos_adyacentes.append(0)
                feromonas_adyacentes.append(0)
            else:
                pesos_adyacentes.append(peso)
                feromonas_adyacentes.append(feromona)
        probabilidades = seleccionarProbabilidades(pesos_adyacentes, feromonas_adyacentes)
        siguiente_ciudad = siguienteCiudad(probabilidades, ciudades_recorridas)
        ciudades_recorridas.append(siguiente_ciudad)

    return ciudades_recorridas

def generarRecorrido(camino):
    '''Devuelve una tupla de tuplas que indican los caminos que siguió la hormiga.
    '''
    recorrido = list()
    for i in range(len(camino) - 1):
        arista = (camino[i], camino[i + 1])
        recorrido.append(arista)

    return recorrido

def actualizarFeromonas(pesos, feromonas, recorridos, tasa_evaporacion, deposito):
    '''Actualiza las feromonas de cada camino entre ciudades.
    '''
    for i in range(6):
        for j in range(6):
            if i == j:
                continue

            m = 0
            for recorrido in recorridos:
                if (i, j) in recorrido:
                    m += 1

            sumatoria = sum([(deposito / 6) for _ in range(m)])
            feromonas[i][j] = (1 - tasa_evaporacion) * feromonas[i][j] + sumatoria

    return feromonas

def calcularCosto(pesos, recorrido):
    '''Calcula el costo de un recorrido.
    '''
    costo = 0
    for arista in recorrido:
        costo += pesos[arista[0]][arista[1]]
    costo += pesos[ recorrido[-1][1] ][ recorrido[0][0] ]
    return costo

def optimizarCamino(pesos, feromonas, hormigas = 2, iteraciones = 2, tasa_evaporacion = 0.3, deposito = 1):
    '''Regresa el mejor recorrido dentro del grafo.
    '''
    for _ in range(iteraciones):
        caminos = [recorrerGrafo(pesos, feromonas, randint(0, 5)) for _ in range(hormigas)]
        recorridos = [generarRecorrido(camino) for camino in caminos]

        feromonas = actualizarFeromonas(pesos, feromonas, recorridos, tasa_evaporacion, deposito)

    from numpy import matrix
    print(matrix(caminos))

    camino_optimo = -1
    maximo = float_info.max
    for indice, recorrido in enumerate(recorridos):
        costo = calcularCosto(pesos, recorrido)
        print(costo)
        if costo < maximo:
            maximo = costo
            camino_optimo = indice
    print('Mejor', maximo)

    return caminos[camino_optimo]