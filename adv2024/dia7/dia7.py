""" Programa que resuelve el día 7 del Advent of Code 2024. """
import os
import itertools
import time

def vprint(verbose, *args):
    if verbose:
        print(*args)

def solve_equation(equation: list[int], verbose: bool = False) -> bool:
    """ Resuelve una ecuación de la forma [resultado, a, b, c, d, ...] 
        devuelve True si se puede encontrar una combinación de operaciones
        de suma y multiplicación que produzca el resultado que será el 
        primer elemento de la lista. 
        Los operadores se resuelven de izquierda a derecha sin tener en cuenta 
        la precedencia habitual de las operaciones."""
    
    target = equation[0]
    numbers = equation[1:]  # Excluimos el primer número que es el resultado buscado
    
    # Crear todas las permutaciones de los operadores
    operators = ['+', '*']
    permutations = list(itertools.product(operators, repeat=len(numbers) - 1))
    
    for permutation in permutations:
        # Empezamos con el primer número
        result = numbers[0]
        expression = [str(numbers[0])]
        
        # Aplicamos cada operador de izquierda a derecha
        for i, op in enumerate(permutation):
            expression.append(op)
            expression.append(str(numbers[i + 1]))
            if op == '+':
                result += numbers[i + 1]
            else:  # op == '*'
                result *= numbers[i + 1]
                
        vprint(verbose, f"result: {result} = {''.join(expression)}")
        if result == target:
            vprint(verbose, f'equation found: {target} = {" ".join(expression)}')
            return True
            
    return False

def solve_equation_2(equation: list[int], verbose: bool = False) -> bool:
    """ Resuelve una ecuación de la forma [resultado, a, b, c, d, ...] 
        devuelve True si se puede encontrar una combinación de operaciones
        de suma y multiplicación que produzca el resultado que será el 
        primer elemento de la lista."""
    
    target = equation[0]
    numbers = equation[1:]
    
    # Crear todas las permutaciones de los operadores
    operators = ['+', '*', '||']
    permutations = list(itertools.product(operators, repeat=len(numbers) - 1))
    
    for permutation in permutations:
        result = numbers[0]
        
        # Optimización: Si el primer número ya es mayor que el objetivo 
        # y solo tenemos operaciones que incrementan, podemos saltar
        if result > target and '||' not in permutation:
            continue
            
        # Para debug, construimos la expresión solo si verbose es True
        if verbose:
            expression = [str(numbers[0])]
        
        # Aplicamos cada operador de izquierda a derecha
        for i, op in enumerate(permutation):
            if verbose:
                expression.append(op)
                expression.append(str(numbers[i + 1]))
                
            if op == '||':
                # Optimización: Precalcular el número de dígitos para evitar conversiones innecesarias
                result = (result * (10 ** len(str(numbers[i + 1])))) + numbers[i + 1]
            elif op == '+':
                result += numbers[i + 1]
            else:  # op == '*'
                result *= numbers[i + 1]
                
            # Optimización: Salir temprano si ya excedemos el objetivo
            if result > target and '||' not in permutation[i+1:]:
                break
        
        if verbose:
            vprint(verbose, f"result: {result} = {''.join(expression)}")
            
        if result == target:
            if verbose:
                vprint(verbose, f'equation found: {target} = {" ".join(expression)}')
            return True
            
    return False

def dia7_1(data, verbose: bool = False):
    """ Función principal del día 7-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        for line in file:
            # Separar el número objetivo y los números de la ecuación
            parts = line.strip().split(':')
            target = int(parts[0])
            numbers = list(map(int, parts[1].split()))
            # Crear la ecuación completa con el objetivo como primer elemento
            equation = [target] + numbers
            vprint(verbose, f'equation: {equation}')
            if solve_equation(equation, verbose):
                result += target
            
    # Imprimir el resultado

    print(f'resultado dia 7 - 1 = "{result}"')
    return result


def dia7_2(data, verbose: bool = False):
    """ Función principal del día 7-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        for line in file:
            # Separar el número objetivo y los números de la ecuación
            parts = line.strip().split(':')
            target = int(parts[0])
            numbers = list(map(int, parts[1].split()))
            # Crear la ecuación completa con el objetivo como primer elemento
            equation = [target] + numbers
            vprint(verbose, f'equation: {equation}')
            if solve_equation(equation, verbose):
                result += target
            elif solve_equation_2(equation, verbose):
                result += target

    # Imprimir el resultado

    print(f'resultado dia 7 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    # Primera parte
    start_time = time.time()
    # assert dia7_1("test7_1.txt", verbose=True) == 3749, "Error se esperaba 3749."
    dia7_1("data7_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 1: {end_time - start_time:.4f} segundos")
    
    # Segunda parte
    start_time = time.time()
    # assert dia7_2("test7_1.txt", verbose=False) == 31, "Error se esperaba 9."
    dia7_2("data7_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 2: {end_time - start_time:.4f} segundos")
