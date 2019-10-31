from constantes import pesos, feromonas
from ant_colony_optimization import recorrerGrafo

def main():
    camino = recorrerGrafo(pesos, feromonas)
    print(camino)

if __name__ == '__main__':
    main()