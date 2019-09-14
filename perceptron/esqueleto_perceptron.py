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

max_iter=50
tasa_aprendizaje=0.1
pesos=[1,0,0,0,0,0,0]
entradas=[[[-1,1,0,1,0,0,0], 1], [[-1,1,0,1,1,0,0], 1], [[-1,1,0,1,0,1,0], 1] 
, [[-1,1,1,0,0,1,1], 1], [[-1,1,1,1,1,0,0], 1], [[-1,1,0,0,0,1,1], 1], [[-1,1,0,0,0,1,0], 0] 
, [[-1,0,1,1,1,0,1], 1], [[-1,0,1,1,0,1,1], 0], [[-1,0,0,0,1,1,0], 0], [[-1,0,1,0,1,0,1], 0], 
[[-1,0,0,0,1,0,1], 0], [[-1,0,1,1,0,1,1], 0], [[-1,0,1,1,1,0,0], 0]]

iter=0
pincorrectos=1.0

while(pincorrectos>0.2 and iter<max_iter):

	incorrectos=0
	
	print()
	print("ITERACION " + str(iter))
	print()

	for entrada in entradas:
		print("Procesando entrada: ")
		print(entrada[0])
		print()
		y=funcion_activacion(funcion_nucleo(pesos,entrada[0]))
		d=entrada[1]
		if y!=d:
			incorrectos=incorrectos+1
			print("ACTUALIZANDO PESOS")
			for i in range(len(pesos)):
				pesos[i]=pesos[i] + 0
				print("w"+str(i) + "=" + str(pesos[i]))
			print()


	pincorrectos=incorrectos*1.0/len(entradas)
	print(str(pincorrectos*100)+"% de entradas procesadas incorrectamente")
	iter=iter+1

print()	
print("Pesos finales:")
print()

for i in range(len(pesos)):
	print("w"+str(i) + "=" + str(pesos[i]))