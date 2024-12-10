import os
import time

def vprint(verbose, *args):
    if verbose:
        print(*args)

def dia10_1(data, verbose: bool = False):
    """ Función principal del día 10-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    origenes = []

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo

        mapa = [list(int(line.strip())) for line in file]
    
    # obtenemos los origenes

    for y, fila in enumerate(mapa):
            for x, altura in enumerate(fila):
                if altura == 0:
                    origenes.append((x, y))
    # Imprimir el resultado
    result = 0
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

