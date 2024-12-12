import os
import time
from typing import Dict, Tuple

def contar_digitos(n: int) -> int:
    if n == 0:
        return 1
    return len(str(n))

def calcular_evolucion(numero: int, blinks: int, cache: Dict[Tuple[int, int], int], verbose: bool = False) -> int:
    """
    Calcula cuántas piedras genera un número después de n parpadeos.
    Usa programación dinámica para evitar cálculos repetidos.
    """
    if blinks == 0:
        return 1  # El número original cuenta como una piedra
    
    # Usar caché si ya calculamos este caso
    key = (numero, blinks)
    if key in cache:
        return cache[key]
    
    # En el primer parpadeo
    if numero == 0:
        # Si es 0, se convierte en 1 y sigue evolucionando
        piedras = calcular_evolucion(1, blinks - 1, cache, verbose)
    elif contar_digitos(numero) % 2 == 0:
        # Si tiene dígitos pares, se divide en dos números
        izq = int(str(numero)[:len(str(numero))//2])
        der = int(str(numero)[len(str(numero))//2:])
        piedras = calcular_evolucion(izq, blinks - 1, cache, verbose) + \
                 calcular_evolucion(der, blinks - 1, cache, verbose)
    else:
        # Si tiene dígitos impares, se multiplica por 2024
        nuevo_num = numero * 2024
        piedras = calcular_evolucion(nuevo_num, blinks - 1, cache, verbose)
    
    # Guardar en caché y retornar
    cache[key] = piedras
    return piedras

def calcular_piedras(numeros: list, blinks: int, verbose: bool = False) -> int:
    """
    Calcula el número total de piedras después de n parpadeos.
    """
    cache = {}
    total_piedras = 0
    
    for i, num in enumerate(numeros):
        if verbose:
            print(f"Procesando número inicial {i+1}/{len(numeros)}: {num}")
        piedras = calcular_evolucion(num, blinks, cache, verbose)
        total_piedras += piedras
        if verbose:
            print(f"  -> Generó {piedras} piedras")
    
    return total_piedras

def dia11_1(data, blinks: int = 25, verbose: bool = False) -> int:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    
    with open(data_path, "r", encoding="utf-8") as file:
        numeros = [int(num) for num in file.readline().split()]
    
    result = calcular_piedras(numeros, blinks, verbose)
    print(f'resultado dia 11 - {1 if blinks <= 25 else 2} = "{result}"')
    return result

def dia11_2(data, verbose: bool = False):
    return dia11_1(data, blinks=75, verbose=verbose)

if __name__ == "__main__":
    start_time = time.time()
    assert dia11_1("test11_1.txt", blinks=6, verbose=True) == 22, "Error se esperaba 22."
    assert dia11_1("test11_1.txt", blinks=25, verbose=False) == 55312, "Error se esperaba 55312."
    dia11_1("data11_1.txt", blinks=25, verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 1: {end_time - start_time:.4f} segundos")
    
    start_time = time.time()
    dia11_2("data11_1.txt", verbose=True)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 2: {end_time - start_time:.4f} segundos")

