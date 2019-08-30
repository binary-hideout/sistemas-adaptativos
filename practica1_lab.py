"""Generar 3 vectores de características para un contexto particular. Utiliza solamente 
2 características para describirlos"""

""" Obtén  la distancia enclidiana entre un par de estos vectores"""

"""EJEMPLO
Contexto-Avengers
vectores- Iron Man, Thor, Cap America
características-fuerza e inteligencia
"""
from math import sqrt
#Contexto Géneros Musicales
Generos=[]
g={'Variedad':.4,'Cant_albums':.5}
Generos.append(g)
g={'Variedad':.7,'Cant_albums':.8}
Generos.append(g)
g={'Variedad':.8,'Cant_albums':.9}
Generos.append(g)

def dist_euclidiana(p1,p2):
    dist= sqrt(((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2))
    print("La distancia euclidiana entre {} y {} es : {} ".format(p1,p2,dist))


print(Generos)
variedad=[]
cantidad=[]
for g in Generos:
    variedad.append(g['Variedad'])
    cantidad.append(g['Cant_albums'])
#PearlJam
g1=[variedad[0],cantidad[0] ]
#TheCure
g2=[variedad[1],cantidad[1]]
#PinkFloyd
g3=[variedad[2],cantidad[2]]
print(variedad)
dist_euclidiana(g1,g2)

"""Saber a que color se parece más """

centroides=[[255,0,0],
    [0,255,0],
    [0,0,255]]

def dist_euclidiana_rgb(p2):
    dist_menor=999
    for c in range(3):
        p1=centroides[c]
        dist= sqrt(((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2) + ((p1[2]-p2[2])**2))
        print("La distancia euclidiana al centroide de {}, para {} es: {} ".format(p2,p1,dist))
        if(dist<dist_menor):
             dist_menor=dist
             x=p1
    print('La menor distancia fue:', dist_menor, ', con el punto: ',x)


dist_euclidiana_rgb([0,253,0])

