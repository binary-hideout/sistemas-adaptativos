from tkinter import Tk, Canvas
from sys import argv

def leerArchivoCL():
    """Leer contenido de un archivo especificado en el segundo argumento de la línea de comandos (CL).
        Regresa el contenido como una lista de cada línea como string.
    """
    try:
        nombre_archivo = argv[1]
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        return [linea.strip() for linea in lineas]
    except IndexError:
        print("Debe especificarse un archivo a leer como primer argumento del comando.")
    except FileNotFoundError:
        print("El archivo '%s' no existe." % nombre_archivo)
    except IOError:
        print("Ocurrió un error al leer el archivo '%s'" % nombre_archivo)
    return None

def main():
    pass

main()