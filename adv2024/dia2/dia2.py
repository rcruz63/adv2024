import os

# funcion para imprimir solo si verbose es True
def vprint(verbose, *args):
    if verbose:
        print(*args)

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
            secure = True
            
            informe = [int(num) for num in line.split()]
            vprint(verbose, informe)  # Imprimir la lista de números para verificar
            
            creciente = informe[0] < informe[1]
            previo = informe[0]
            for index, numero in enumerate(informe):
                vprint(verbose, f'previo: {previo}, numero: {numero}, creciente: {creciente}')
                if index == 0:
                    continue
                if  not (0 < abs(numero - previo) < 4):
                    secure = False
                    break
                if creciente and numero < previo:
                    secure = False
                    break
                if not creciente and numero > previo:
                    secure = False
                    break
                previo = numero
                
            if secure:
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
        num_line = 1
        jugadas = []
        for line in file:
            # Decodificar la linea
            pass

    # Imprimir el resultado

    print(f'resultado dia 2 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    # assert dia2_1("test2_1.txt", verbose=True) == 2, "Error se esperaba 2."
    dia2_1("data2_1.txt", verbose=False)
    # assert dia2_2("test2_1.txt", verbose=False) == 31, "Error se esperaba 9."
    # dia2_2("data2_1.txt", verbose=True)
