import os
import time
import sys

def vprint(verbose, *args):
    if verbose:
        print(*args)

def validar_antinodo(antinodo, max_x, max_y):
    x, y = antinodo
    return 0 <= x < max_x and 0 <= y < max_y

def calcular_antinodos(coordenada1, coordenada2, max_x, max_y, verbose):
    x1, y1 = coordenada1
    x2, y2 = coordenada2
    vprint(verbose, f'{coordenada1} - {coordenada2}')
    dx = x2 - x1
    dy = y2 - y1
    
    antinodos = []
    aninodo1 = (x1 - dx, y1 - dy)
    aninodo2 = (x2 + dx, y2 + dy)
    vprint(verbose, aninodo1, aninodo2)
    if validar_antinodo(aninodo1, max_x, max_y):
        vprint(verbose, 'aninodo1 valido')
        antinodos.append(aninodo1)
    if validar_antinodo(aninodo2, max_x, max_y):
        vprint(verbose, 'aninodo2 valido')
        antinodos.append(aninodo2)

    return antinodos

def calcular_antinodos_2(coordenada1, coordenada2, max_x, max_y, verbose):
    x1, y1 = coordenada1
    x2, y2 = coordenada2
    vprint(verbose, f'{coordenada1} - {coordenada2}')
    dx = x2 - x1
    dy = y2 - y1
    
    antinodos = []

    antinodo_superior = (x1 - dx, y1 - dy)
    vprint(verbose, f'antinodo_superior = {antinodo_superior}')
    while validar_antinodo(antinodo_superior, max_x, max_y):
        antinodos.append(antinodo_superior)
        antinodo_superior = (antinodo_superior[0] - dx, antinodo_superior[1] - dy)
        vprint(verbose, f'antinodo_superior = {antinodo_superior}')
    
    antinodo_inferior = (x2 + dx, y2 + dy)
    vprint(verbose, f'antinodo_inferior = {antinodo_inferior}')
    while validar_antinodo(antinodo_inferior, max_x, max_y):
        antinodos.append(antinodo_inferior)
        antinodo_inferior = (antinodo_inferior[0] + dx, antinodo_inferior[1] + dy)
        vprint(verbose, f'antinodo_inferior = {antinodo_inferior}')

    return antinodos

def dia8_1(data, verbose: bool = False):
    """ Función principal del día 8-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        mapa = [list(line.strip()) for line in file]

    max_x = len(mapa[0])
    max_y = len(mapa)

    # generar un diccionario de caracteres validos y sus coordenadas
    caracteres_validos = {}
    for y, row in enumerate(mapa):
        for x, char in enumerate(row):
            if char != '.':
                caracteres_validos[char] = caracteres_validos.get(char, []) + [(x, y)]

    max_caracteres = len(caracteres_validos)
    print(f'max_caracteres = {max_caracteres}')
    vprint(caracteres_validos)
    # Para cada caracter valido, calcular los antinodos generados
    # para cada par de coordenadas habra dos antinodos,
    # se debe calcular la distancia entre los dos puntos y
    # colocar un antinodo en linea con los nodos a la misma distancia
    # que la calculada
    antinodos = []
    count = 0
    for char, coordenadas in caracteres_validos.items():
        print(f'{char} = {coordenadas} {count}/{max_caracteres}')
        count += 1
        max_coordenadas = len(coordenadas)
        for i in range(max_coordenadas):
            print(f'{i}/{max_coordenadas}')
            for j in range(i+1, max_coordenadas):
                antinodos.extend(calcular_antinodos(coordenadas[i], coordenadas[j], max_x, max_y, verbose))
        
    vprint(antinodos)
    # Eliminar antinodos repetidos
    antinodos = list(set(antinodos))
            
    # Imprimir el resultado
    result = len(antinodos)
    print(f'resultado dia 8 - 1 = "{result}"')
    return result


def dia8_2(data, verbose: bool = False):
    """ Función principal del día 8-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        mapa = [list(line.strip()) for line in file]

    max_x = len(mapa[0])
    max_y = len(mapa)

    # generar un diccionario de caracteres validos y sus coordenadas
    caracteres_validos = {}
    for y, row in enumerate(mapa):
        for x, char in enumerate(row):
            if char != '.':
                caracteres_validos[char] = caracteres_validos.get(char, []) + [(x, y)]

    max_caracteres = len(caracteres_validos)
    print(f'max_caracteres = {max_caracteres}')
    vprint(caracteres_validos)
    # Para cada caracter valido, calcular los antinodos generados
    # para cada par de coordenadas habra dos antinodos,
    # se debe calcular la distancia entre los dos puntos y
    # colocar un antinodo en linea con los nodos a la misma distancia
    # que la calculada
    antinodos = []
    count = 0
    for char, coordenadas in caracteres_validos.items():
        print(f'{char} = {coordenadas} {count}/{max_caracteres}')
        count += 1
        max_coordenadas = len(coordenadas)
        antinodos.extend(coordenadas)
        for i in range(max_coordenadas):
            print(f'{i}/{max_coordenadas}')
            for j in range(i+1, max_coordenadas):
                antinodos.extend(calcular_antinodos_2(coordenadas[i], coordenadas[j], max_x, max_y, verbose))
        
    vprint(antinodos)
    # Eliminar antinodos repetidos
    antinodos = list(set(antinodos))
            
    # Imprimir el resultado
    result = len(antinodos)
    # Imprimir el resultado

    print(f'resultado dia 8 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    start_time = time.time()
    # assert dia8_1("test8_1.txt", verbose=True) == 14, "Error se esperaba 14."
    # dia8_1("data8_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 1: {end_time - start_time:.4f} segundos")
    start_time = time.time()
    # assert dia8_2("test8_1.txt", verbose=True) == 34, "Error se esperaba 34."
    dia8_2("data8_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 2: {end_time - start_time:.4f} segundos")

