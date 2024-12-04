import os

def vprint(verbose, *args):
    if verbose:
        print(*args)


def process_state_machine(data, verbose=False):
    """
    Máquina de estados para procesar un string y calcular la suma de productos de 
    todas las secuencias `mul(dd,dd)`.

    Args:
        data (str): String de datos a procesar.

    Example:
        result = process_state_machine("mul(123,456) mul(10,20)")
        print(result)  # 56088 + 200 = 56288

    Returns:
        int: Suma de los productos de todas las secuencias encontradas.
    """
    state = "start"
    num1 = ""
    num2 = ""
    total_sum = 0

    # Tabla de estados
    transitions = {
        "start": lambda char: ("state_m" if char == "m" else ("state_d" if char == "d" else "start")),
        "state_m": lambda char: "state_u" if char == "u" else ("state_m" if char == "m" else "start"),
        "state_u": lambda char: "state_l" if char == "l" else ("state_m" if char == "m" else "start"),
        "state_l": lambda char: "state_open_paren" if char == "(" else ("state_m" if char == "m" else "start"),
        "state_open_paren": lambda char: ("state_num1" if char.isdigit() else ("state_m" if char == "m" else "start")),
        "state_num1": lambda char: ("state_num1" if char.isdigit() else "state_comma" if char == "," else ("state_m" if char == "m" else "start")),
        "state_comma": lambda char: ("state_num2" if char.isdigit() else ("state_m" if char == "m" else "start")),
        "state_num2": lambda char: ("state_num2" if char.isdigit() else "start" if char == ")" else ("state_m" if char == "m" else "start")),
        "state_d": lambda char: "state_i" if char == "i" else ("state_m" if char == "m" else "start"),
    }

    for char in data:
        if state == "state_open_paren" and char.isdigit():
            num1 += char
        elif state == "state_num1" and char.isdigit():
            num1 += char
        elif state == "state_comma" and char.isdigit():
            num2 += char
        elif state == "state_num2" and char.isdigit():
            num2 += char
        elif state == "state_num2" and char == ")":
            # Calcula el producto y suma al total
            total_sum += int(num1) * int(num2)
            vprint(verbose, f"mul({num1},{num2}) = {int(num1) * int(num2)}")
            num1, num2 = "", ""
        # Transición de estado
        state = transitions[state](char)
        if state == "start":
            num1, num2 = "", ""

    return total_sum


def dia3_1(data, verbose: bool = False):
    """ Función principal del día 3-1. """

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
            result += process_state_machine(line, verbose)

    # Imprimir el resultado

    print(f'resultado dia 3 - 1 = "{result}"')
    return result


def dia3_2(data, verbose: bool = False):
    """ Función principal del día 3-2. """

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

    print(f'resultado dia 3 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    # assert dia3_1("test3_1.txt", verbose=True) == 161, "Error se esperaba 161."
    dia3_1("data3_1.txt", verbose=False)
    # assert dia3_2("test3_1.txt", verbose=False) == 31, "Error se esperaba 9."
    # dia3_2("data3_1.txt", verbose=True)
