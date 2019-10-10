'''
 Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software
 
 Programacion de Sistemas Adaptativos
 Automatas celulares
 Automata con celdas binarias, donde cada celda tiene dos vecinos (1D)
'''

def imprime_resultado(cadena):
'''Imprimir resultado con el formato establecido: 0=blanco, 1=*.
Entrada: cadena.
Salida: cadena con formato establecido (anexa guiones al principio y al final).'''
    resultado_formato = '_'
    for caracter in cadena:
        if caracter == '1':
            resultado_formato += '*'
        else:
            resultado_formato += ' '
    print(resultado_formato + "_")

# Aplicar la regla con la ventana recibida.
# Entrada: Ventana (coleccion de tres celdas, la central y dos vecinos a los lados)
# Salida: 0 o 1, dependiendo de la regla utilizada

# Regla 0: Cualquier cosa = 0
#def procesa_ventana(ventana):
#    return '0'

# Regla 51: Color contrario a la celda central, i.e. 0=1, 1=0
#def procesa_ventana(ventana):
#    if ventana[1]=='0':
#        resultado='1'
#    elif ventana[1]=='1':
#        resultado='0'
#    return resultado

# Regla 165: Vecinos con el mismo color=1, de otra manera=0    
def procesa_ventana(ventana):
    if ventana[0] == ventana[2]:
        resultado = '1'
    else:
        resultado = '0'
    return resultado

# Generar una nueva cadena de acuerdo a una regla (0-255)
# Entrada: cadena actual (t=i)
# Salida: cadena nueva (t=i+1)
def recorre_cadena(cadena):
    nueva_cadena = ''

    for i in range(0, len(cadena)):
        n = len(cadena)
        ventana = cadena[(i + (n - 1)) % n] + cadena[i] + cadena[(i + 1) % n]
        nueva_cadena += procesa_ventana(ventana)
            
    return nueva_cadena

def correr(iteraciones):
	#-------------------------------------------------------------
	#Procedimiento para probar el AC

	# Cadenas de prueba
	cadena1 = "0000000000000000000000000000000000100000000000000000000000000000000000"
	#cadena2 = "0000100000"

	cadena_actual = cadena1

	# Toma la cantidad de iteraciones como argumento de la linea de comando
	#iteraciones = sys.argv[1]

	# Por la cantidad fijada de iteraciones:
	#   Imprime la cadena actual
	#   Genera una nueva cadena de acuerdo a la regla
	#   Reemplaza la cadena actual por esta nueva cadena
	for i in range(0, int(iteraciones)):
		imprime_resultado(cadena_actual)
		nueva_cadena = recorre_cadena(cadena_actual)
		cadena_actual = nueva_cadena
