from sys import argv

def calcular(lines):
	n = len(lineas)
	m = 0
	grados = list()

	for linea in lineas:
		linea = linea.strip()
		celdas = linea.split()
		grado = 0
		for celda in celdas:
			m += int(celda)
			grado += int(celda)
		grados.append(grado)
	m /= 2

	densidad = (2 * m) / (n * (n - 1))

	print('n (cantidad de nodos):', n)
	print('m (cantidad de aristas):', m)
	print('Densidad:', densidad)

	for indice, grado in enumerate(grados):
		centralidad = grado / (n - 1)
		print("Grado v%d = %g\tCentralidad: %g" % (indice, grado, centralidad))

try:
	with open(argv[1],'r') as archivo:
		lineas = archivo.readlines()
	calcular(lineas)
except IOError:
	print('No se pudo abrir el archivo')