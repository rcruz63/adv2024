import os

# funcion para imprimir solo si verbose es True
def vprint(verbose, *args):
    if verbose:
        print(*args)


def is_safe(informe, verbose):
    safe = True
    creciente = informe[0] < informe[1]
    previo = informe[0]
    for index, numero in enumerate(informe):
        vprint(verbose, f'previo: {previo}, numero: {numero}, creciente: {creciente}')
        if index == 0:
            continue
        if  not (0 < abs(numero - previo) < 4):
            safe = False
            break
        if creciente and numero < previo:
            safe = False
            break
        if not creciente and numero > previo:
            safe = False
            break
        previo = numero
    return safe


def dia2_1(data, verbose: bool = False):
    """ Función principal del día 2-1. """

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

            informe = [int(num) for num in line.split()]
            vprint(verbose, informe)  # Imprimir la lista de números para verificar

            safe = is_safe(informe, verbose)

            if safe:
                result += 1

    # Imprimir el resultado

    print(f'resultado dia 2 - 1 = "{result}"')
    return result


def dia2_2(data, verbose: bool = False):
    """ Función principal del día 2-2. """

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
            
            informe = [int(num) for num in line.split()]
            vprint(verbose, informe)  # Imprimir la lista de números para verificar
            
            safe = is_safe(informe, verbose)

            if not safe:
                for index, _ in enumerate(informe):
                    # crear una nueva lista con todos los elementos menos el actual
                    new_informe = informe[:index] + informe[index+1:]
                    new_safe = is_safe(new_informe, verbose)
                    if new_safe:
                        safe = True
                        break

            if safe:
                result += 1

    # Imprimir el resultado

    print(f'resultado dia 2 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    # assert dia2_1("test2_1.txt", verbose=True) == 2, "Error se esperaba 2."
    # dia2_1("data2_1.txt", verbose=False)
    # assert dia2_2("test2_2.txt", verbose=True) == 6, "Error se esperaba 6."
    dia2_2("data2_1.txt", verbose=False)
