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
import sys

def calcularDistanciaEuclideana(puntoA, puntoB):
    ''' (A) Primer funcion a completar 
    Entradas: puntoA y puntoB -- son listas numericas de cualquier longitud (debe ser la misma longitud en ambas listas).
    Salida: Distancia euclidiana entre las listas.''' 
    return sqrt((puntoB[0] - puntoA[0]) ** 2 + (puntoB[1] - puntoA[1]) ** 2 + (puntoB[2] - puntoA[2]) ** 2)

def actualizarCentroide(datos, grupos, indiceCentroide):
    ''' (B) Segunda funcion a completar
    Entradas:
        datos -- lista anidada donde cada sublista es un vector de caracteristicas
        grupos -- lista numerica que contiene, para cada vector en datos, cual es el grupo al que corresponde
        indiceCentroide -- centroide a actualizarCentroide
        Salida: lista que contiene los nuevos valores para el centroide cuyo indice es indiceCentroide
    '''
    pass

datos = ((153, 51, 255), (121, 236, 221), (209, 236, 121), (240, 164, 76), (240, 98, 76), (76, 93, 240), (50, 239, 94))
centroides = ((255, 0, 0), (0, 255, 0), (0, 0, 255)) #Inicializacion de centroides

grupos = []

# (C) Bloque de codigo: Calculo de distancias y asignacion de grupos
# AQUI EMPIEZA TU CODIGO

print(grupos)

# (D) Bloque de codigo: Actualizacion de centroides
# AQUI EMPIEZA TU CODIGO

print(centroides) #Imprime centroides actualizados
