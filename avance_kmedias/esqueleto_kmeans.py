'''
INSTRUCCIONES: Completa la primera iteracion de k-medias. Para ello, utiliza la siguiente informacion y el esqueleto que a continuacion se te presenta.

Algunas funciones importantes:

 len(lista)
Devuelve la cantidad de elementos que tiene lista (si es lista anidada, serian los elementos del primer nivel).

 range(desde donde, hasta donde, cuanto avanzar)
Se utiliza junto con ciclos para determinar de que valor a que valor ira la variable del ciclo. Si solo usamos range(hasta donde), se asume que se empieza desde cero y se avanza uno.

 sys.float_info.max [Usar libreria sys]
Regresa el numero mas grande de punto flotante que tiene registrado Python

 pow(numero, potencia) [Usar libreria math]
Eleva numero a la potencia indicada.

'''

from math import sqrt
from sys import float_info
from random import randint

def calcularDistanciaEuclideana(puntoA, puntoB):
    ''' (A) Primer funcion a completar 
    Entradas: puntoA y puntoB -- son listas numericas de cualquier longitud (debe ser la misma longitud en ambas listas).
    Salida: Distancia euclidiana entre las listas.'''
    dimension = len(puntoA)
    suma = 0.0
    for i in range(dimension):
        suma += (puntoB[i] - puntoA[i]) ** 2
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
    for i in range(len(datos[0])):
        suma = 0.0
        cantidad = 0
        for indice, muestra in enumerate(datos):
            if grupos[indice] == indiceCentroide:
                suma += muestra[i]
                cantidad += 1
        nuevo_centroide.append(suma / cantidad)
    return tuple(nuevo_centroide)
    

def centroideMasCercano(centroides, muestra):
    '''Recibe una 'muestra' que almacena un elemento de una colección de datos y 'centroides' que almacena una colección de los centroides.
    Regresa 'k' que es la posición del centroide más cercano.
    '''
    menor = float_info.max
    for i in range(3):
        dist = calcularDistanciaEuclideana(muestra, centroides[i])
        if dist < menor:
            menor = dist
            k = i
    return k

datos = ((153, 51, 255), (121, 236, 221), (209, 236, 121), (240, 164, 76), (240, 98, 76), (76, 93, 240), (50, 239, 94))
centroides = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] #Inicializacion de centroides

grupos = list()

# (C) Bloque de codigo: Calculo de distancias y asignacion de grupos
for i in range(len(datos)):
    pertenencia = centroideMasCercano(centroides, datos[i])
    grupos.append(pertenencia)

print(grupos)

# (D) Bloque de codigo: Actualizacion de centroides
for i in range(len(centroides)):
    centroides[i] = actualizarCentroide(datos, grupos, i)

print(centroides) #Imprime centroides actualizados

print('\nArchivo de datos:')
data = list()
with open('datos_nivel_bonus.txt.txt', 'r') as file:
    for line in file.readlines():
        sample = [int(num) for num in line.split()]
        data.append(sample)

