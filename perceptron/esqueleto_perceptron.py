def funcion_nucleo(pesos, entrada):
	#1--COMPLETA AQUI EL RESTO DE LA FUNCION

def funcion_activacion(resultado_nucleo):
	#2--COMPLETA AQUI EL RESTO DE LA FUNCION

		
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
				pesos[i]=pesos[i] + #3--COMPLETA AQUI LO QUE FALTA
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