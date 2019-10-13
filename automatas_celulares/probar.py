'''
 Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software
 
 Programacion de Sistemas Adaptativos
 Automatas celulares
 Programa para visualizar una regla del AC 1D
'''

from sys import argv
from reglas import correr

iteraciones = int(argv[1])
correr(iteraciones)