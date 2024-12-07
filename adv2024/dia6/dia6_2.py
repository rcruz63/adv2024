import os
from typing import List, Tuple, Set

def vprint(verbose, *args):
    if verbose:
        print(*args)

def encontrar_guardia(mapa: List[List[str]], verbose: bool = False) -> Tuple[int, int]:
    for y, linea in enumerate(mapa):
        for x, char in enumerate(linea):
            if char in ['^', 'v', '>', '<']:
                return x, y
    raise ValueError("No se encontró el guardia en el mapa")

def guardia_dentro_mapa(x: int, y: int, mapa: List[List[str]]) -> bool:
    return 0 <= y < len(mapa) and 0 <= x < len(mapa[y])

def mover_guardia(x: int, y: int, mapa: List[List[str]]) -> Tuple[int, int]:
    orientacion = mapa[y][x]
    
    # Calcular nueva posición según orientación
    if orientacion == '^': nuevo_x, nuevo_y = x, y - 1
    elif orientacion == 'v': nuevo_x, nuevo_y = x, y + 1
    elif orientacion == '>': nuevo_x, nuevo_y = x + 1, y
    elif orientacion == '<': nuevo_x, nuevo_y = x - 1, y
    else: raise ValueError(f"Orientación no válida: {orientacion}")
    
    # Si está fuera del mapa, retornar nueva posición
    if not guardia_dentro_mapa(nuevo_x, nuevo_y, mapa):
        return nuevo_x, nuevo_y
    
    # Si hay obstáculo, rotar 90 grados a la derecha
    if mapa[nuevo_y][nuevo_x] == '#':
        if orientacion == '^': nueva_orientacion = '>'
        elif orientacion == '>': nueva_orientacion = 'v'
        elif orientacion == 'v': nueva_orientacion = '<'
        elif orientacion == '<': nueva_orientacion = '^'
        mapa[y][x] = nueva_orientacion
        return x, y
    
    # Mover y actualizar orientación (sin marcar con 'X')
    orientacion_actual = mapa[y][x]  # Guardamos la orientación actual
    mapa[nuevo_y][nuevo_x] = orientacion_actual  # La copiamos en la nueva posición
    return nuevo_x, nuevo_y

def detectar_ciclo_floyd(x0: int, y0: int, mapa_original: List[List[str]], verbose: bool = False) -> bool:
    """
    Implementa el algoritmo de Floyd (tortuga y liebre) para detectar ciclos.
    Más eficiente que guardar todos los estados visitados.
    """
    # Crear una copia del mapa para no modificar el original
    mapa = [fila[:] for fila in mapa_original]
    
    # Inicializar tortuga y liebre en la posición inicial
    tortuga_x, tortuga_y = x0, y0
    liebre_x, liebre_y = x0, y0
    
    # Contador de pasos para evitar bucles infinitos
    pasos = 0
    max_pasos = len(mapa) * len(mapa[0]) * 4  # Un límite razonable
    
    while pasos < max_pasos:
        pasos += 1
        
        # Mover tortuga una vez
        if not guardia_dentro_mapa(tortuga_x, tortuga_y, mapa):
            return False
        tortuga_x, tortuga_y = mover_guardia(tortuga_x, tortuga_y, mapa)
        
        # Verificar si la tortuga sigue dentro después de moverse
        if not guardia_dentro_mapa(tortuga_x, tortuga_y, mapa):
            return False
            
        # Mover liebre dos veces
        for _ in range(2):
            if not guardia_dentro_mapa(liebre_x, liebre_y, mapa):
                return False
            liebre_x, liebre_y = mover_guardia(liebre_x, liebre_y, mapa)
            
            # Verificar si la liebre sigue dentro después de moverse
            if not guardia_dentro_mapa(liebre_x, liebre_y, mapa):
                return False
        
        # Si coinciden posición y orientación, hay un ciclo
        if (tortuga_x, tortuga_y, mapa[tortuga_y][tortuga_x]) == \
           (liebre_x, liebre_y, mapa[liebre_y][liebre_x]):
            return True
    
    return False  # Si llegamos aquí, no encontramos ciclo en max_pasos

def dia6_2(data: str, verbose: bool = False) -> int:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    
    # Leer y procesar el mapa
    with open(data_path, "r", encoding="utf-8") as file:
        mapa = [list(line.strip()) for line in file]
    
    num_filas, num_columnas = len(mapa), len(mapa[0])
    print(f"MAPA: filas = {num_filas}, columnas = {num_columnas}")
    
    # Obtener camino original
    mapa_original = [fila[:] for fila in mapa]
    x0, y0 = encontrar_guardia(mapa, verbose)
    camino_original: Set[Tuple[int, int]] = set()
    x, y = x0, y0
    
    while guardia_dentro_mapa(x, y, mapa):
        camino_original.add((x, y))
        x, y = mover_guardia(x, y, mapa)
    
    # Encontrar posiciones adyacentes al camino
    posiciones_a_probar: Set[Tuple[int, int]] = set()
    for x, y in camino_original:
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if (guardia_dentro_mapa(nx, ny, mapa_original) and 
                mapa_original[ny][nx] == '.' and 
                (nx, ny) != (x0, y0)):
                posiciones_a_probar.add((nx, ny))
    
    # Probar cada posición
    result = 0
    for x, y in posiciones_a_probar:
        vprint(verbose, f"\nProbando obstáculo en ({x}, {y})")
        mapa = [fila[:] for fila in mapa_original]  # Nueva copia limpia para cada prueba
        mapa[y][x] = '#'
        if detectar_ciclo_floyd(x0, y0, mapa, verbose):
            result += 1
            vprint(verbose, f"Encontrado ciclo con obstáculo en ({x}, {y})")
    
    print(f'resultado dia 6 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    assert dia6_2("test6_1.txt", verbose=True) == 6, "Error: se esperaban 6 posiciones"
    assert dia6_2("data6_1.txt", verbose=False) == 1697, "Error: se esperaban 1697 posiciones"