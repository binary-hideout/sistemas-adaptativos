from numpy import ones, fill_diagonal

feromonas = ones((6, 6), int)
fill_diagonal(feromonas, 0)
feromonas = list([list(_) for _ in feromonas])

distancias = list()
# Valle Rocco
distancias.append([0, 20, 10, 33, 8, 2])
# Isla Banshee
distancias.append([20, 0, 6, 15, 5, 3])
# Hongolandia
distancias.append([10, 6, 0, 24, 23, 13])
# Fontana
distancias.append([33, 15, 24, 0, 17, 7])
# Koopalandia
distancias.append([8, 5, 23, 17, 0, 22])
# Springfield
distancias.append([2, 3, 13, 7, 22, 0])
pesos = [d for d in distancias]