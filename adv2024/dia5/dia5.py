import os

def vprint(verbose, *args):
    if verbose:
        print(*args)

def load_data(data_path, verbose: bool = False) -> tuple[list, list]:
    """ Cargar los datos del archivo. """

    reglas = []
    updates = []

    with open(data_path, "r", encoding="utf-8") as file:
        rules = True
        # Leer cada linea del archivo
        for line in file:
            # Decodificar la linea
            line = line.strip()
            if line == "":
                rules = False
                continue
            if rules:
                # Es una regla
                regla = [int(num) for num in line.split("|")]
                reglas.append(regla)
            else:
                # Es un update
                update = [int(num) for num in line.split(",")]
                updates.append(update)

    vprint(verbose, f'reglas = {reglas}')
    vprint(verbose, f'updates = {updates}')

    return reglas, updates

def check_update(update, reglas, verbose: bool = False) -> bool:
    """ Verificar si un update es válido. """

    result = True
    for i, num in enumerate(update):
        for j, num2 in enumerate(update):
            if i == j:
                continue
            if i > j:
                if [num2, num] in reglas:
                    vprint(verbose, f'[{num2}, {num}] in reglas')
                    continue
                else:
                    vprint(verbose, f'[{num2}, {num}] not in reglas')
                    result = False
                    break
            if [num, num2] in reglas:
                vprint(verbose, f'[{num}, {num2}] in reglas')
                continue
            vprint(verbose, f'[{num}, {num2}] not in reglas')
            result = False
            break
        if not result:
            break
    vprint(verbose, f'update = {update}, result = {result}')

    return result

def dia5_1(data, verbose: bool = False):
    """ Función principal del día 5-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    reglas, updates = load_data(data_path, verbose)

    result = 0
    updates_valid = []
    for update in updates:
        if check_update(update, reglas, verbose):
            updates_valid.append(update)
    vprint(verbose, f'updates_valid = {updates_valid}')

    for update in updates_valid:
        result += update[len(update) // 2]
            
    # Imprimir el resultado

    print(f'resultado dia 5 - 1 = "{result}"')
    return result


def dia5_2(data, verbose: bool = False):
    """ Función principal del día 5-2. """

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

    print(f'resultado dia 5 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    # assert dia5_1("test5_1.txt", verbose=True) == 143, "Error se esperaba 143."
    dia5_1("data5_1.txt", verbose=False)
    # assert dia5_2("test5_1.txt", verbose=False) == 31, "Error se esperaba 9."
    # dia5_2("data5_1.txt", verbose=True)
