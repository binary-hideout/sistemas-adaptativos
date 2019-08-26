from sys import argv

cesar3={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}

#generar_cifrador, funcion que recibe un valor de tipo entero 
# y se encarga de crear un diccionario con la llave-valor del cifrador. (Parte A)
def generar_cifrador(offset):
    #se declara e instancia una variable de tipo lista que contiene todos los caracteres del alfabeto.
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #se declara e instancia un diccionario donde va a guardar las reglas para el cifrado que se genere.
    offset_dict = {}
    #loop que recorre todos los caracteres de las letras.
    for char in letras:
        #if-else que revisa si nuestro indice actual del ciclo + offset se pasan de la cantidad de elementos de la lista.
        if (letras.index(char) + offset) >= len(letras):
            offset_dict[char] = letras[letras.index(char) + offset - len(letras)]
        else:
            offset_dict[char] = letras[letras.index(char) + offset]
    return offset_dict

#cifrar, recibe una variable de tipo string y otra de tipo diccionario. (Parte B)
def cifrar(palabra, cifrador):
    #se declara e instancia una variable de tipo string donde se va a asignar el resultado del cifrado.
    string_cifrado = ''
    #loop que recorre cada caracter de la palabra.
    for char in palabra:
        #se asegura que el caracter sea parte de las llaves dentro de nuestro diccionario.
        if char in cifrador.keys():
            string_cifrado += cifrador[char]
        #de lo contrario, simplemente se agrega el caracter normal.
        else:
            string_cifrado += char
    return string_cifrado

#mostrar_cifrador, se trata de una funcion que imprime los datos cifrados, guardados en un diccionaro. (Parte C)
def mostrar_cifrador(nombre_partes, cifrador, curp):
    nombre = ''
    #loop que recorre cada elemento de la lista nombre_partes.
    for partes in nombre_partes:
        #agrega cada parte de la lista a la variable de tipo string nombre, tambien utiliza el metodo lower().
        nombre += (partes + " ").lower()
    #guarda todos los valores con sus respectivas llaves en un diccionario, como lo establece la parte C.
    usuario_datos = {'Nombre': nombre, 'Nombre cifrado': cifrar(nombre, cesar3), 'Nombre cifrado con N desfase': cifrar(nombre, cifrador), 'CURP': curp}
    #loop que utiliza el metodo items() la cual retorna la llave y su valor.
    for key, value in usuario_datos.items():
        print(key + ": " + value)

#leer_archivo, funcion que recibe un archivo y el desfase para generar el cifrador de N desfase.
#TODO: Buscar una mejor manera de organizar esta funcion.
def leer_archivo(file, desfase):
    with open(file) as file_object:
        lines = file_object.readlines()
        for line in lines:
            nombre_partes = line.split()
    curp = ''
    if len(nombre_partes) == 3:
        nombre = nombre_partes[0]
        primer_apellido = nombre_partes[1]
        segundo_apellido = nombre_partes[2]
        curp = (primer_apellido[:2] + segundo_apellido[:1] + nombre[:1]).upper()
    else:
        nombre = nombre_partes[0]
        primer_apellido = nombre_partes[2]
        segundo_apellido = nombre_partes[3]
        curp = (primer_apellido[:2] + segundo_apellido[:1] + nombre[:1]).upper()
    cifrador = generar_cifrador(desfase)
    mostrar_cifrador(nombre_partes, cifrador, curp)

try:
    file = argv[1]
except:
    file = "name.txt"

try:
    argv_cantidad = int(argv[2])
except:
    argv_cantidad = 3

leer_archivo(file, argv_cantidad)
