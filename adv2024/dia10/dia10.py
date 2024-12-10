import os
import time

def vprint(verbose, *args):
    if verbose:
        print(*args)

def next_step(mapa, origen, max_x, max_y, finales_visitados, verbose=False) -> int:
    x, y = origen
    altura = mapa[y][x]

    vprint(verbose, f"\nExplorando posición ({x}, {y}) con altura {altura}")

    if altura == 9:
        if (x, y) not in finales_visitados:
            finales_visitados.add((x, y))
            vprint(verbose, f"¡Encontrado final en ({x}, {y})!")
            return 1
        return 0
    
    # Marcamos esta posición como visitada temporalmente
    valor_original = mapa[y][x]
    mapa[y][x] = -1  # marcamos como visitado

    caminos = 0
    # Norte    
    if y > 0 and mapa[y - 1][x] == altura + 1:
        vprint(verbose, f"Explorando Norte desde ({x}, {y})")
        caminos += next_step(mapa, (x, y - 1), max_x, max_y, finales_visitados, verbose)
    # Sur
    if y < max_y - 1 and mapa[y + 1][x] == altura + 1:
        vprint(verbose, f"Explorando Sur desde ({x}, {y})")
        caminos += next_step(mapa, (x, y + 1), max_x, max_y, finales_visitados, verbose)
    # Este
    if x < max_x - 1 and mapa[y][x + 1] == altura + 1:
        vprint(verbose, f"Explorando Este desde ({x}, {y})")
        caminos += next_step(mapa, (x + 1, y), max_x, max_y, finales_visitados, verbose)
    # Oeste
    if x > 0 and mapa[y][x - 1] == altura + 1:
        vprint(verbose, f"Explorando Oeste desde ({x}, {y})")
        caminos += next_step(mapa, (x - 1, y), max_x, max_y, finales_visitados, verbose)
    
    # Restauramos el valor original
    mapa[y][x] = valor_original
    
    vprint(verbose, f"Total caminos desde ({x}, {y}): {caminos}")
    return caminos

def next_step2(mapa, origen, max_x, max_y, verbose=False) -> int:
    x, y = origen
    altura = mapa[y][x]

    vprint(verbose, f"\nExplorando posición ({x}, {y}) con altura {altura}")

    if altura == 9:
        vprint(verbose, f"¡Encontrado final en ({x}, {y})!")
        return 1
    
    # Marcamos esta posición como visitada temporalmente
    valor_original = mapa[y][x]
    mapa[y][x] = -1  # marcamos como visitado

    caminos = 0
    # Norte    
    if y > 0 and mapa[y - 1][x] == altura + 1:
        vprint(verbose, f"Explorando Norte desde ({x}, {y})")
        caminos += next_step2(mapa, (x, y - 1), max_x, max_y, verbose)
    # Sur
    if y < max_y - 1 and mapa[y + 1][x] == altura + 1:
        vprint(verbose, f"Explorando Sur desde ({x}, {y})")
        caminos += next_step2(mapa, (x, y + 1), max_x, max_y, verbose)
    # Este
    if x < max_x - 1 and mapa[y][x + 1] == altura + 1:
        vprint(verbose, f"Explorando Este desde ({x}, {y})")
        caminos += next_step2(mapa, (x + 1, y), max_x, max_y, verbose)
    # Oeste
    if x > 0 and mapa[y][x - 1] == altura + 1:
        vprint(verbose, f"Explorando Oeste desde ({x}, {y})")
        caminos += next_step2(mapa, (x - 1, y), max_x, max_y, verbose)
    
    # Restauramos el valor original
    mapa[y][x] = valor_original
    
    vprint(verbose, f"Total caminos desde ({x}, {y}): {caminos}")
    return caminos

def dia10_1(data, verbose: bool = False):
    """ Función principal del día 10-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    vprint(verbose, f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        mapa = [[int(c) for c in line.strip()] for line in file]

    vprint(verbose, "Mapa inicial:")
    if verbose:
        for fila in mapa:
            print(fila)

    # obtenemos los origenes
    rutas = []
    for y, fila in enumerate(mapa):
        for x, altura in enumerate(fila):
            if altura == 0:
                rutas.append((x, y))

    vprint(verbose, f"Puntos de inicio encontrados: {rutas}")
    
    # Imprimir el resultado
    result = 0
    max_x = len(mapa[0])
    max_y = len(mapa)
    for i, origen in enumerate(rutas):
        vprint(verbose, f"\nExplorando ruta {i+1} desde origen {origen}")
        finales_visitados = set()  # Conjunto para registrar los finales visitados desde este origen
        caminos = next_step(mapa, origen, max_x, max_y, finales_visitados, verbose)
        vprint(verbose, f"Total caminos para origen {origen}: {caminos}")
        result += caminos
        
    print(f'resultado dia 10 - 1 = "{result}"')
    return result


def dia10_2(data, verbose: bool = False):
    """ Función principal del día 10-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    vprint(verbose, f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        mapa = [[int(c) for c in line.strip()] for line in file]

    vprint(verbose, "Mapa inicial:")
    if verbose:
        for fila in mapa:
            print(fila)

    # obtenemos los origenes
    rutas = []
    for y, fila in enumerate(mapa):
        for x, altura in enumerate(fila):
            if altura == 0:
                rutas.append((x, y))

    vprint(verbose, f"Puntos de inicio encontrados: {rutas}")
    
    # Imprimir el resultado
    result = 0
    max_x = len(mapa[0])
    max_y = len(mapa)
    for i, origen in enumerate(rutas):
        vprint(verbose, f"\nExplorando ruta {i+1} desde origen {origen}")
        caminos = next_step2(mapa, origen, max_x, max_y, verbose)
        vprint(verbose, f"Total caminos para origen {origen}: {caminos}")
        result += caminos
        
    print(f'resultado dia 10 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    start_time = time.time()
    # assert dia10_1("test10_1.txt", verbose=True) == 36, "Error se esperaba 36."
    # dia10_1("data10_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 1: {end_time - start_time:.4f} segundos")
    start_time = time.time()
    # assert dia10_2("test10_1.txt", verbose=True) == 81, "Error se esperaba 81."
    dia10_2("data10_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 2: {end_time - start_time:.4f} segundos")

