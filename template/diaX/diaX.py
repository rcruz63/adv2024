import os

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
    assert diaX_1("testX_1.txt", verbose=False) == 11, "Error se esperaba 11."
    # diaX_1("dataX_1.txt", verbose=False)
    # assert diaX_2("testX_1.txt", verbose=False) == 31, "Error se esperaba 9."
    # diaX_2("dataX_1.txt", verbose=True)
