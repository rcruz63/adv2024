import os

def vprint(verbose, *args):
    if verbose:
        print(*args)


def process_state_machine2(data, verbose=False):
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

    enabled = True

    def define_start(char):
        return "state_d" if char == "d" else ("state_m" if (char == "m" and enabled) else "start")

    # Tabla de estados
    transitions = {
        "start": define_start,
        "state_m": lambda char: "state_u" if char == "u" else define_start(char),
        "state_u": lambda char: "state_l" if char == "l" else define_start(char),
        "state_l": lambda char: "state_open_paren" if char == "(" else define_start(char),
        "state_open_paren": lambda char: ("state_num1" if char.isdigit() else define_start(char)),
        "state_num1": lambda char: ("state_num1" if char.isdigit() else "state_comma" if char == "," else define_start(char)),
        "state_comma": lambda char: ("state_num2" if char.isdigit() else define_start(char)),
        "state_num2": lambda char: "state_num2" if char.isdigit() else define_start(char),
        "state_d": lambda char: "state_o" if char == "o" else define_start(char),
        "state_o": lambda char: "state_n" if char == "n" else "state_do" if char == '(' else define_start(char),
        "state_n": lambda char: "state_up" if char == "'" else define_start(char),
        "state_up": lambda char: "state_t" if char == "t" else define_start(char),
        "state_t": lambda char: "state_dont" if char == "(" else define_start(char),
        "state_do": define_start,
        "state_dont": define_start,
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
        elif state == "state_do" and char == ")":
            vprint(verbose, "Enabled")
            enabled = True
        elif state == "state_dont" and char == ")":
            vprint(verbose, "Disabled")
            enabled = False
        elif state == "state_num2" and char == ")":
            # Calcula el producto y suma al total
            total_sum += int(num1) * int(num2)
            vprint(verbose, f"mul({num1},{num2}) = {int(num1) * int(num2)}")
            num1, num2 = "", ""
        # Transición de estado
        state = transitions[state](char)
        if state in ["start", "state_m", "state_d"]:
            num1, num2 = "", ""

    return total_sum


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
        "start": lambda char: ("state_m" if char == "m" else "start"),
        "state_m": lambda char: "state_u" if char == "u" else ("state_m" if char == "m" else "start"),
        "state_u": lambda char: "state_l" if char == "l" else ("state_m" if char == "m" else "start"),
        "state_l": lambda char: "state_open_paren" if char == "(" else ("state_m" if char == "m" else "start"),
        "state_open_paren": lambda char: ("state_num1" if char.isdigit() else ("state_m" if char == "m" else "start")),
        "state_num1": lambda char: ("state_num1" if char.isdigit() else "state_comma" if char == "," else ("state_m" if char == "m" else "start")),
        "state_comma": lambda char: ("state_num2" if char.isdigit() else ("state_m" if char == "m" else "start")),
        "state_num2": lambda char: ("state_num2" if char.isdigit() else "start" if char == ")" else ("state_m" if char == "m" else "start")),
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
        lines = file.readlines()

    data = "".join(lines)
    result = process_state_machine2(data, verbose)

    # Imprimir el resultado

    print(f'resultado dia 3 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    # assert dia3_1("test3_1.txt", verbose=True) == 161, "Error se esperaba 161."
    # dia3_1("data3_1.txt", verbose=False)
    # assert dia3_2("test3_2.txt", verbose=True) == 48, "Error se esperaba 48."
    dia3_2("data3_1.txt", verbose=True)
