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

def generarDiccionario():
    """Genera un diccionario de colores.
    """
    return {
        'a' : '#ffff00',
        'c' : '#00ffff',
        'd' : '#ffc90e',
        'm' : '#800080',
        'r' : '#ff0000',
        'v' : '#00bb00'
    }

def generarVentana(filas, diccionario):
    """Genera una ventana del juego Flood-It con los colores especificados en el argumento. Debe ser lista de strings.
    """
    root = Tk()
    canvas = Canvas(root, width = 280, height = 280)

    x1, y1, x2, y2 = 0, 0, 20, 20
    for fila in filas:
        for color in fila:
            canvas.create_rectangle(x1, y1, x2, y2, fill = diccionario[color], outline = "")
            x1 += 20
            x2 += 20
        x1, x2 = 0, 20
        y1 += 20
        y2 += 20
    canvas.pack()
    return canvas

def main():
    contenido = leerArchivoCL()
    diccionario = generarDiccionario()
    canvas = generarVentana(contenido, diccionario)
    canvas.mainloop()

main()