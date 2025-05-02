# TSP con Hill Climbing Iterativo

import math
import random

# Coordenadas de las ciudades
coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

# Calcular la distancia entre dos coordenadas
def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Calcular la distancia total de una ruta
def evalua_ruta(ruta):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    # Agregar la distancia de la última ciudad a la primera
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

# Algoritmo de Hill Climbing Iterativo
def i_hill_climbing():
    # Crear ruta inicial aleatoria
    ruta = list(coord.keys())
    mejor_ruta = ruta[:]
    max_iteraciones = 10  # Número máximo de iteraciones

    while max_iteraciones > 0:
        mejora = True
        # Generar nueva ruta aleatoria
        random.shuffle(ruta)
        while mejora:
            mejora = False
            dist_actual = evalua_ruta(ruta)
            # Evaluar vecinos
            for i in range(len(ruta)):
                if mejora:
                    break
                for j in range(i + 1, len(ruta)):  # Evitar intercambios redundantes
                    if i != j:
                        # Crear una nueva ruta intercambiando dos ciudades
                        ruta_tmp = ruta[:]
                        ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                        dist = evalua_ruta(ruta_tmp)
                        if dist < dist_actual:
                            # Se encontró un vecino que mejora el resultado
                            mejora = True
                            ruta = ruta_tmp[:]
                            break

        # Actualizar la mejor ruta encontrada
        if evalua_ruta(ruta) < evalua_ruta(mejor_ruta):
            mejor_ruta = ruta[:]

        # Decrementar el contador de iteraciones
        max_iteraciones -= 1

    return mejor_ruta

if __name__ == "__main__":
    # Ejecutar el algoritmo de Hill Climbing Iterativo
    ruta = i_hill_climbing()
    print("Ruta óptima encontrada:")
    print(ruta)
    print("Distancia Total: " + str(evalua_ruta(ruta)))