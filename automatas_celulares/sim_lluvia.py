'''
 Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software
 
 Programacion de Sistemas Adaptativos
 Automatas celulares
 Programa que simula una lluvia de meteoritos utilizando automatas celulares
'''

from sys import argv
from meteor import crear_meteoro
from reglas import recorre_cadena

posiciones = [[100, 100], [100, 500], [200, 300], [200, 400], [300, 100], [300, 300], [300, 600], [400, 300], [400, 500], [500, 200], [500, 600]]
configuracion_actual = "00000100000"

if (len(argv) < 2):
	for i in range(len(posiciones)):
		crear_meteoro(posiciones[i][0], posiciones[i][1])
else:
	iteraciones = int(argv[1])
	for i in range(iteraciones):
		print(configuracion_actual)
		j = 0
		for celda in configuracion_actual:
			if int(celda) == 1:
				crear_meteoro(posiciones[j][0], posiciones[j][1])
			j = j + 1
		nueva_configuracion = recorre_cadena(configuracion_actual)
		configuracion_actual = nueva_configuracion