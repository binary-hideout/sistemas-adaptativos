from numpy import ones, fill_diagonal

# crear matriz de numpy rellena con unos, de 6 x 6
feromonas = ones((6, 6), int)
# poner la diagonal principal en ceros
fill_diagonal(feromonas, 0)
# cambiar el tipo de la matriz a listas nativas de Python
feromonas = list([list(_) for _ in feromonas])

distancias = list()
# 0. Valle Rocco
distancias.append([0, 20, 10, 33, 8, 2])
# 1. Isla Banshee
distancias.append([20, 0, 6, 15, 5, 3])
# 2. Hongolandia
distancias.append([10, 6, 0, 24, 23, 13])
# 3. Fontana
distancias.append([33, 15, 24, 0, 17, 7])
# 4. Koopalandia
distancias.append([8, 5, 23, 17, 0, 22])
# 5. Springfield
distancias.append([2, 3, 13, 7, 22, 0])
# 6. matriz de pesos
pesos = [d for d in distancias]