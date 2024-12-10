import os
import time

def vprint(verbose, *args):
    if verbose:
        print(*args)

def next_step(mapa, origen, max_x, max_y, verbose=False) -> int:
    x, y = origen
    altura = mapa[y][x]

    vprint(verbose, f"altura: {altura} - (x, y): ({x}, {y})")

    if altura == 9:
        return 1

    caminos = 0
    # Norte    
    if y > 0 and mapa[y - 1][x] == altura + 1:
        caminos += next_step(mapa, (x, y - 1), max_x, max_y, verbose)
    # Sur
    if y < max_y - 1 and mapa[y + 1][x] == altura + 1:
        caminos += next_step(mapa, (x, y + 1), max_x, max_y, verbose)
    # Este
    if x < max_x - 1 and mapa[y][x + 1] == altura + 1:
        caminos += next_step(mapa, (x + 1, y), max_x, max_y, verbose)
    # Oeste
    if x > 0 and mapa[y][x - 1] == altura + 1:
        caminos += next_step(mapa, (x - 1, y), max_x, max_y, verbose)
    
    vprint(verbose, caminos)
    return caminos

def dia10_1(data, verbose: bool = False):
    """ Función principal del día 10-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    rutas = []

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        mapa = [[int(c) for c in line.strip()] for line in file]

    vprint(verbose, f"mapa: {mapa}")
    # obtenemos los origenes

    for y, fila in enumerate(mapa):
            for x, altura in enumerate(fila):
                if altura == 0:
                    rutas.append((x, y))

    vprint(verbose, f"rutas: {rutas}")
    # Imprimir el resultado
    result = 0
    max_x = len(mapa[0])
    max_y = len(mapa)
    for origen in rutas:
        result += next_step(mapa, origen, max_x, max_y)
    print(f'resultado dia 10 - 1 = "{result}"')
    return result


def dia10_2(data, verbose: bool = False):
    """ Función principal del día 10-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        num_line = 1
        jugadas = []
        for line in file:
            # Decodificar la linea
            pass

    # Imprimir el resultado

    print(f'resultado dia 10 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    start_time = time.time()
    assert dia10_1("test10_1.txt", verbose=True) == 36, "Error se esperaba 36."
    # dia10_1("data10_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 1: {end_time - start_time:.4f} segundos")
    start_time = time.time()
    # assert dia10_2("test10_1.txt", verbose=True) == 31, "Error se esperaba 9."
    # dia10_2("data10_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 2: {end_time - start_time:.4f} segundos")

