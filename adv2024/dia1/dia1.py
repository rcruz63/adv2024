import os

def dia1_1(data, verbose: bool = False):
    """ Función principal del día 1-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        lefts = []
        rights = []
        for line in file:
            # Decodificar la linea
            left, right = line.split()
            lefts.append(int(left))
            rights.append(int(right))

    lefts.sort()
    rights.sort()

    for index, left in enumerate(lefts):
        # print(index, left, rights[index])
        result += abs(left - rights[index])

    # Imprimir el resultado

    print(f'resultado dia 1 - 1 = "{result}"')

    return result


def dia1_2(data, verbose: bool = False):
    """ Función principal del día 1-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        lefts = []
        rights = []
        for line in file:
            # Decodificar la linea
            left, right = line.split()
            lefts.append(int(left))
            rights.append(int(right))

        for _, left in enumerate(lefts):
            # contar cuantas veces aparece left en el lista rights
            count = rights.count(left)
            # print(left, count)
            result += left * count


    # Imprimir el resultado

    print(f'resultado dia 1 - 2 = "{result}"')

    return result

if __name__ == "__main__":
    # assert dia1_1("test1_1.txt", verbose=False) == 11, "Error se esperaba 11."
    # dia1_1("data1_1.txt", verbose=False)
    # assert dia1_2("test1_1.txt", verbose=False) == 31, "Error se esperaba 9."
    dia1_2("data1_1.txt", verbose=True)
