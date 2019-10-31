from constantes import pesos, feromonas
from ant_colony_optimization import optimizarCamino

def main():
    camino = optimizarCamino(pesos, feromonas, 50, 100)
    print(camino)

if __name__ == '__main__':
    main()