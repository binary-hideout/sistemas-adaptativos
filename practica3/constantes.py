from numpy import ones, fill_diagonal

feromonas = ones((6, 6), int)
fill_diagonal(feromonas, 0)
feromonas = list([list(_) for _ in feromonas])

distancias = [list() for _ in range(6)]
distancias[0] = [0, 20, 10, 33, 8, 2]
distancias[1] = [20, 0, 6, 15, 5, 3]
distancias[2] = [10, 6, 0, 24, 23, 13]
distancias[3] = [33, 15, 24, 0, 17, 7]
distancias[4] = [8, 5, 23, 17, 0, 22]
distancias[5] = [2, 3, 13, 7, 22, 0]
pesos = [d for d in distancias]

TASA_EVAPORACION = 0.3
DEPOSITO = 1
HORMIGAS = 2