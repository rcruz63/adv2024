import os
import time

def vprint(verbose, *args):
    if verbose:
        print(*args)

def diaX_1(data, verbose: bool = False):
    """ Función principal del día X-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        for line in file:
            # Decodificar la linea
            pass
            
    # Imprimir el resultado

    print(f'resultado dia X - 1 = "{result}"')
    return result


def diaX_2(data, verbose: bool = False):
    """ Función principal del día X-2. """

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

    print(f'resultado dia X - 2 = "{result}"')
    return result

if __name__ == "__main__":
    start_time = time.time()
    assert diaX_1("testX_1.txt", verbose=True) == 11, "Error se esperaba 11."
    # diaX_1("dataX_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 1: {end_time - start_time:.4f} segundos")
    start_time = time.time()
    # assert diaX_2("testX_1.txt", verbose=True) == 31, "Error se esperaba 9."
    # diaX_2("dataX_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 2: {end_time - start_time:.4f} segundos")

