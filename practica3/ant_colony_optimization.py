from random import randint, random
from sys import float_info

def siguienteCiudad(probabilidades, ciudades_recorridas):
    '''Selecciona la siguiente ciudad.

    probabilidades: lista de probabilidades de ir a cada ciudad.

    ciudades_recorridas: lista de ciudades previamente visitadas.
    '''
    # número aleatorio a partir del cual escoger la ciudad
    num_aleatorio = random()
    # límite del rango de probabilidades designadas a cada ciudad
    suma = 0
    for ciudad, probabilidad in enumerate(probabilidades):
        suma += probabilidad
        # si la ciudad no se ha visitado,
        # y el número aleatorio está dentro del rango de probabilidades de la ciudad actual
        if ciudad not in ciudades_recorridas and num_aleatorio < suma:
            # siguiente ciudad a visitar
            return ciudad

def seleccionarProbabilidades(pesos, feromonas):
    '''Calcula las probabilidades para escoger a la siguiente ciudad, de las que son adyacentes a la actual.

    pesos: lista filtrada de pesos adyacentes de la ciudad actual.

    feromonas: lista filtrada de feromonas adyacentes de la ciudad actual.
    '''
    # lista de las aptitudes de cada ciudad adyacente a la actual
    aptitudes = [(feromona / peso) if peso != 0 else 0 for peso, feromona in zip(pesos, feromonas)]
    # suma de las aptitudes
    total = sum(aptitudes)

    # lista de las probabilidades para cada ciudad adyacente
    probabilidades = [(a / total) for a in aptitudes]
    return probabilidades

def recorrerGrafo(pesos, feromonas, ciudad_inicial):
    '''Hace un recorrido por el grafo.

    pesos: matriz de pesos.

    feromonas: matriz de feromonas.

    ciudad_inicial: primera ciudad visitada.
    '''
    # iniciar lista de las ciudades recorridas
    ciudades_recorridas = [ciudad_inicial]

    # visitar las ciudades restantes
    for _ in range(5):
        # la ciudad actual es la última de la lista
        ciudad_actual = ciudades_recorridas[-1]

        # filtrar los pesos y feromonas que son adyacentes a la ciudad actual
        pesos_adyacentes, feromonas_adyacentes = list(), list()
        for (ciudad, peso), feromona in zip(enumerate(pesos[ciudad_actual]), feromonas[ciudad_actual]):
            # si la ciudad ya fue visitada
            if ciudad in ciudades_recorridas:
                # peso y feromona en 0 para omitirla
                pesos_adyacentes.append(0)
                feromonas_adyacentes.append(0)
            # si no se ha visitado la ciudad
            else:
                pesos_adyacentes.append(peso)
                feromonas_adyacentes.append(feromona)
        # calcular probabilidades de selección
        probabilidades = seleccionarProbabilidades(pesos_adyacentes, feromonas_adyacentes)
        # seleccionar siguiente ciudad
        siguiente_ciudad = siguienteCiudad(probabilidades, ciudades_recorridas)
        # agregar ciudad visitada para descartarla en las siguientes selecciones
        ciudades_recorridas.append(siguiente_ciudad)
    # regresar lista del orden de visita
    return ciudades_recorridas

def generarRecorrido(camino):
    '''Devuelve una tupla de tuplas que indican los caminos que siguió la hormiga.

    camino: lista de las ciudades recorridas.
    '''
    # lista del recorrido
    recorrido = list()
    for i in range(len(camino) - 1):
        # tupla en formato (origen, destino)
        arista = (camino[i], camino[i + 1])
        recorrido.append(arista)
    # regresar recorrido en formato (A, B), (B, C) etc
    return recorrido

def actualizarFeromonas(pesos, feromonas, recorridos, tasa_evaporacion, deposito):
    '''Actualiza las feromonas de cada arista entre ciudades.

    pesos: matriz de pesos.

    feromonas: matriz de feromonas.

    recorridos: lista de recorridos.
    '''
    # iterar sobre cada celda/arista de la matriz de feromonas
    for i in range(6):
        for j in range(6):
            # si la celda está en la diagonal principal
            # (si la ciudad es la misma)
            if i == j:
                # siguiente celda
                continue
            
            # cantidad de hormigas que han pasado por la arista actual i,j
            m = 0
            for recorrido in recorridos:
                # si la arista actual sí fue recorrida
                if (i, j) in recorrido:
                    # incrementar cantidad de hormigas
                    m += 1
            sumatoria = sum([(deposito / 6) for _ in range(m)])
            # actualizar arista actual
            feromonas[i][j] = (1 - tasa_evaporacion) * feromonas[i][j] + sumatoria
    # regresar matriz de feromonas actualizada
    return feromonas

def calcularCosto(pesos, recorrido):
    '''Calcula el costo de un recorrido.

    pesos: matriz de pesos.

    recorrido: lista del recorrido.
    '''
    costo = 0
    # iterar sobre las aristas del recorrido
    for arista in recorrido:
        # sumar peso de la arista actual
        costo += pesos[arista[0]][arista[1]]
    # sumar peso entre la última ciudad visitada y la primera (regreso)
    costo += pesos[ recorrido[-1][1] ][ recorrido[0][0] ]
    return costo

def optimizarCamino(pesos, feromonas, hormigas = 2, iteraciones = 2, tasa_evaporacion = 0.3, deposito = 1):
    '''Calcula el mejor recorrido dentro del grafo.

    pesos: matriz de pesos.

    feromonas: matriz de feromonas.

    hormigas: cantidad de hormigas para recorrer el grafo.

    iteraciones: vueltas que dará cada hormiga.
    '''
    # hacer algoritmo ACO 'iteraciones' veces
    for _ in range(iteraciones):
        # lista de los caminos de cada hormiga en formato A, B, C etc
        # cada camino se actualiza en cada iteración, influenciados por el ajuste de feromonas
        caminos = [recorrerGrafo(pesos, feromonas, randint(0, 5)) for _ in range(hormigas)]
        # lista de los recorridos de cada hormiga en formato (A, B), (B, C) etc
        recorridos = [generarRecorrido(camino) for camino in caminos]
        # ajuste de la matriz de feromonas
        feromonas = actualizarFeromonas(pesos, feromonas, recorridos, tasa_evaporacion, deposito)
    # índice del mejor camino
    camino_optimo = -1
    # menor costo encontrado
    ## nombre irónico
    maximo = float_info.max
    # iterar los recorridos finales de cada hormiga
    for indice, recorrido in enumerate(recorridos):
        # calcular costo del recorrido actual
        costo = calcularCosto(pesos, recorrido)
        print(costo)
        # si el costo actual es menor al mejor
        if costo < maximo:
            # actualizar mejor costo
            maximo = costo
            # actualizar índice del mejor camino
            camino_optimo = indice
    print('Mejor', maximo)
    # regresar el mejor camino encontrado
    return caminos[camino_optimo]