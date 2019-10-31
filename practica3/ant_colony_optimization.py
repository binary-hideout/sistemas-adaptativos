from random import randint, random

def siguienteCiudad(probabilidades, ciudades_recorridas):
    '''Selecciona la siguiente ciudad.
    '''
    num_aleatorio = random()
    print('Random', num_aleatorio)
    suma = 0
    for ciudad, probabilidad in enumerate(probabilidades):
        suma += probabilidad
        print('Ciudad', ciudad)
        print('Suma', suma)
        if ciudad not in ciudades_recorridas and num_aleatorio < suma:
            return ciudad

def seleccionarProbabilidades(pesos, feromonas):
    '''Calcula las probabilidades para cada ciudad a escoger.
    '''
    aptitudes = [(feromona / peso) if peso != 0 else 0 for peso, feromona in zip(pesos, feromonas)]
    total = sum(aptitudes)
    probabilidades = [(a / total) for a in aptitudes]

    return probabilidades

def optimizarRecorrido(pesos, feromonas, tasa_evaporacion = 0.3, deposito = 1, hormigas = 2):
    '''Regresa el mejor recorrido encontrado dentro de la matriz 'pesos'.
    '''
    ciudades_recorridas = [randint(0, 5)]

    for _ in range(5):
        print(ciudades_recorridas)
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
        print(pesos_adyacentes)
        probabilidades = seleccionarProbabilidades(pesos_adyacentes, feromonas_adyacentes)
        print(probabilidades)
        siguiente_ciudad = siguienteCiudad(probabilidades, ciudades_recorridas)
        ciudades_recorridas.append(siguiente_ciudad)

    return ciudades_recorridas