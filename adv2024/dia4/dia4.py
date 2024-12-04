import os

def vprint(verbose, *args):
    if verbose:
        print(*args)

def buscar_horizontal(tablero, palabra, verbose):
    result = 0
    for _, line in enumerate(tablero):
        result += line.count(palabra)
        vprint(verbose, f"line = {line}, palabra = {palabra}, count = {line.count(palabra)}")
    vprint(verbose, f"buscar_horizontal({palabra}) = {result}")
    return result

def obtener_diagonales(tabla):
    """
    Convierte una tabla en una nueva tabla formada por sus diagonales.
    Las filas diagonales se rellenan con puntos (.) donde sea necesario.

    Args:
        tabla (list[str]): Matriz original representando la sopa de letras.

    Returns:
        list[str]: Tabla formada por las diagonales de la matriz original.
    """
    filas, columnas = len(tabla), len(tabla[0])
    diagonales = []

    # Diagonales desde la esquina superior izquierda hacia abajo
    for inicio_fila, _ in enumerate(tabla):
        diagonal = []
        i, j = inicio_fila, 0
        while i < filas and j < columnas:
            diagonal.append(tabla[i][j])
            i += 1
            j += 1
        diagonales.append("".join(diagonal))

    for inicio_col, _ in enumerate(tabla[0][1:], start=1):  # Excluye la columna inicial
        diagonal = []
        i, j = 0, inicio_col
        while i < filas and j < columnas:
            diagonal.append(tabla[i][j])
            i += 1
            j += 1
        diagonales.append("".join(diagonal))

    # Diagonales desde la esquina superior derecha hacia abajo
    for inicio_fila, _ in enumerate(tabla):
        diagonal = []
        i, j = inicio_fila, columnas - 1
        while i < filas and j >= 0:
            diagonal.append(tabla[i][j])
            i += 1
            j -= 1
        diagonales.append("".join(diagonal))

    for inicio_col, _ in enumerate(tabla[0][:-1]):  # Excluye la última columna
        diagonal = []
        i, j = 0, inicio_col
        while i < filas and j >= 0:
            diagonal.append(tabla[i][j])
            i += 1
            j -= 1
        diagonales.append("".join(diagonal))

    return diagonales


def dia4_1(data, verbose: bool = False):
    """ Función principal del día 4-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        sopa = [line.strip() for line in file]
        
    result = buscar_horizontal(sopa, "XMAS", verbose)
    result += buscar_horizontal(sopa, "SAMX", verbose)

    # Trasponer la sopa
    sopa_t = ["".join(row) for row in zip(*sopa)]
    result += buscar_horizontal(sopa_t, "XMAS", verbose)
    result += buscar_horizontal(sopa_t, "SAMX", verbose)

    # Formar una lista con las diagonales, rellenar con '.' para que todas tengan la misma longitud
    sopa_d = obtener_diagonales(sopa)
    result += buscar_horizontal(sopa_d, "XMAS", verbose)
    result += buscar_horizontal(sopa_d, "SAMX", verbose)
       
    # Imprimir el resultado

    print(f'resultado dia 4 - 1 = "{result}"')
    return result


def dia4_2(data, verbose: bool = False):
    """ Función principal del día 4-2. """

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

    print(f'resultado dia 4 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    # assert dia4_1("test4_1.txt", verbose=True) == 18, "Error se esperaba 18."
    dia4_1("data4_1.txt", verbose=False)
    # assert dia4_2("test4_1.txt", verbose=False) == 31, "Error se esperaba 9."
    # dia4_2("data4_1.txt", verbose=True)
