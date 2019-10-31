from constantes import pesos, feromonas
from ant_colony_optimization import optimizarRecorrido

def main():
    camino = optimizarRecorrido(pesos, feromonas)
    print(camino)

if __name__ == '__main__':
    main()