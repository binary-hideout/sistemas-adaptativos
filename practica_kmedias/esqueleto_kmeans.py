'''
INSTRUCCIONES: Completa la primera iteracion de k-medias. Para ello, utiliza la siguiente informacion y el esqueleto que a continuacion se te presenta.
'''

from math import sqrt
from sys import float_info
from random import randint

def calcularDistanciaEuclideana(puntoA, puntoB):
    ''' (A) Primer funcion a completar 
    Entradas: puntoA y puntoB -- son listas numericas de cualquier longitud (debe ser la misma longitud en ambas listas).
    Salida: Distancia euclidiana entre las listas.'''
    suma = 0
    for A, B in zip(puntoA, puntoB):
        suma += (B - A) ** 2
    return sqrt(suma)

def actualizarCentroide(datos, grupos, indiceCentroide):
    ''' (B) Segunda funcion a completar
    Entradas:
        datos -- lista anidada donde cada sublista es un vector de caracteristicas
        grupos -- lista numerica que contiene, para cada vector en datos, cual es el grupo al que corresponde
        indiceCentroide -- centroide a actualizarCentroide
        Salida: lista que contiene los nuevos valores para el centroide cuyo indice es indiceCentroide
    '''
    nuevo_centroide = list()
    dimension = len(datos[0])
    for d in range(dimension):
        suma = 0.0
        cantidad = 0
        for indice, muestra in enumerate(datos):
            if grupos[indice] == indiceCentroide:
                suma += muestra[d]
                cantidad += 1
        nuevo_centroide.append(suma / cantidad)
    return tuple(nuevo_centroide)

def centroideMasCercano(centroides, muestra):
    '''Recibe una 'muestra' que almacena un elemento de una colección de datos y 'centroides' que almacena una colección de los centroides.
    Regresa 'k' que es la posición del centroide más cercano.
    '''
    menor = float_info.max
    for indice, centroide in enumerate(centroides):
        dist = calcularDistanciaEuclideana(muestra, centroide)
        if dist < menor:
            menor = dist
            cercano = indice
    return cercano

def agrupar(datos, centroides):
    '''Agrupa los datos y actualiza centroides.
    '''
    print('Centroides originales:')
    print(centroides)
    grupos = list()

    # (C) Bloque de codigo: Calculo de distancias y asignacion de grupos
    for muestra in datos:
        pertenencia = centroideMasCercano(centroides, muestra)
        grupos.append(pertenencia)

    print('Grupos de pertenencia:')
    print(grupos)

    # (D) Bloque de codigo: Actualizacion de centroides
    for i in range(len(centroides)):
        centroides[i] = actualizarCentroide(datos, grupos, i)
    
    print('Centroides actualizados:')
    print(centroides) #Imprime centroides actualizados

print('\n-----Colores-----')
datos = ((153, 51, 255), (121, 236, 221), (209, 236, 121), (240, 164, 76), (240, 98, 76), (76, 93, 240), (50, 239, 94))
centroides = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] #Inicializacion de centroides
agrupar(datos, centroides)

print('\n-----Archivo de datos-----')
data = list()
with open('datos_nivel_bonus.txt', 'r') as file:
    for line in file.readlines():
        temp = [int(num) for num in line.split()]
        data.append(temp)

centers = [data[randint(0, 149)] for i in range(5)]
agrupar(data, centers)