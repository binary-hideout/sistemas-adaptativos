from random import random

def funcion_nucleo(pesos, entrada):
	'''Calcula la suma ponderada de 2 listas.

	pesos: lista que almacena los valores de los pesos.

	entrada: lista que almacena los valores de una entrada.
	'''
	return sum([w * x for w, x in zip(pesos, entrada)])

def funcion_activacion(resultado_nucleo):
	'''Aplica la función escalonada.

	resultado_nucleo: parámetro para la función.
	'''
	return 1 if resultado_nucleo >= 0 else 0

# aleatorizar pesos iniciales
pesos = [random() for _ in range(7)]
# matriz de entradas
entradas = [[-1, 1, 0, 1, 0, 0, 0],
			[-1, 1, 0, 1, 1, 0, 0],
			[-1, 1, 0, 1, 0, 1, 0], 
			[-1, 1, 1, 0, 0, 1, 1], 
			[-1, 1, 1, 1, 1, 0, 0], 
			[-1, 1, 0, 0, 0, 1, 1],
			[-1, 1, 0, 0, 0, 1, 0],
			[-1, 0, 1, 1, 1, 0, 1],
			[-1, 0, 1, 1, 0, 1, 1],
			[-1, 0, 0, 0, 1, 1, 0],
			[-1, 0, 1, 0, 1, 0, 1], 
			[-1, 0, 0, 0, 1, 0, 1],
			[-1, 0, 1, 1, 0, 1, 1],
			[-1, 0, 1, 1, 1, 0, 0]]
# salidas esperadas
salidas = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]

max_iter = 100
tasa_aprendizaje = 0.1
iteracion = 0
pincorrectos = 1
while pincorrectos > 0 and iteracion < max_iter:
	print("\nITERACION %d" % iteracion)
	incorrectos = 0

	# entrenamiento
	for entrada, salida in zip(entradas, salidas):
		print("\nProcesando entrada:", entrada)
		print("Salida esperada:", salida)

		# predecir la salida de la entrada actual
		prediccion = funcion_activacion(funcion_nucleo(pesos, entrada))
		print("Predicción:", prediccion)
		# comparar la predicción con la salida esperada
		if prediccion != salida:
			incorrectos += 1

			print("\n-----ACTUALIZANDO PESOS-----")
			error = salida - prediccion
			for i, x_i in zip(range(len(pesos)), entrada):
				# nuevo peso
				pesos[i] += tasa_aprendizaje * x_i * error
				print("w%d = %g" % (i, pesos[i]))
	pincorrectos = incorrectos * 1.0 / len(entradas)
	iteracion += 1

print("\n%g%% de entradas procesadas incorrectamente" % (pincorrectos * 100))

print("\nPesos finales:")
for i, w in enumerate(pesos):
	print("w%d = %g" % (i, pesos[i]))