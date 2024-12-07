import os

def vprint(verbose, *args):
    if verbose:
        print(*args)

def encontrar_guardia(mapa, verbose: bool = False) -> tuple[int, int]:
    """ Encontrar la posición inicial del guardia. """

    for y, linea in enumerate(mapa):
        for x, char in enumerate(linea):
            if char in ['^', 'v', '>', '<']:
                return x, y

def guardia_dentro_mapa(x, y, mapa) -> bool:
    """ Verificar si el guardia está dentro del mapa. """

    return y >= 0 and y < len(mapa) and x >= 0 and x < len(mapa[y])

def mover_guardia(x, y, mapa, verbose: bool = False) -> tuple[int, int]:
    """ Mover el guardia según el protocolo. """
    
    orientacion = mapa[y][x]
    mapa[y][x] = 'X'  # Marcamos la posición actual
    
    # Intentamos hasta 4 direcciones (una vuelta completa)
    nueva_orientacion = orientacion
    vprint(verbose, f'nueva_orientacion = {nueva_orientacion}')
    while True:
        # Calculamos la nueva posición según la orientación actual
        if nueva_orientacion == '^':
            nuevo_x, nuevo_y = x, y - 1
        elif nueva_orientacion == 'v':
            nuevo_x, nuevo_y = x, y + 1
        elif nueva_orientacion == '>':
            nuevo_x, nuevo_y = x + 1, y
        elif nueva_orientacion == '<':
            nuevo_x, nuevo_y = x - 1, y
        
        # Si la posición está fuera del mapa, esa es nuestra salida
        if not guardia_dentro_mapa(nuevo_x, nuevo_y, mapa):
            return nuevo_x, nuevo_y
            
        # Si hay obstáculo, rotamos 90 grados a la derecha y continuamos
        if mapa[nuevo_y][nuevo_x] == '#':
            if nueva_orientacion == '^': nueva_orientacion = '>'
            elif nueva_orientacion == '>': nueva_orientacion = 'v'
            elif nueva_orientacion == 'v': nueva_orientacion = '<'
            elif nueva_orientacion == '<': nueva_orientacion = '^'
            continue
        
        # Si llegamos aquí, la posición es válida y no hay obstáculo
        mapa[nuevo_y][nuevo_x] = nueva_orientacion
        return nuevo_x, nuevo_y

def dia6_1(data, verbose: bool = False):
    """ Función principal del día 6-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        mapa = []
        for line in file:
            # Decodificar la linea
            line = line.strip()
            vprint(verbose, line)
            mapa.append(list(line))
            vprint(verbose, mapa[-1])
    vprint(verbose, mapa)
    
    x0, y0 = encontrar_guardia(mapa, verbose)
    vprint(verbose, f'x0 = {x0}, y0 = {y0}')
    x, y = x0, y0
    while guardia_dentro_mapa(x, y, mapa):
        x, y = mover_guardia(x, y, mapa, verbose)
        vprint(verbose, f'x = {x}, y = {y}')

    # Contar todas las 'X' en cada fila del mapa
    result = sum(fila.count('X') for fila in mapa)
            
    print(f'resultado dia 6 - 1 = "{result}"')
    return result


def dia6_2(data, verbose: bool = False):
    """ Función principal del día 6-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        mapa = []
        for line in file:
            # Decodificar la linea
            line = line.strip()
            vprint(verbose, line)
            mapa.append(list(line))
            vprint(verbose, mapa[-1])
    vprint(verbose, mapa)
    num_filas = len(mapa)
    num_columnas = len(mapa[0])
    print(f"MAPA:filas = {num_filas}, columnas = {num_columnas}")
    # Guardar el mapa original
    mapa_original = [fila[:] for fila in mapa]
    result = 0
    x0, y0 = encontrar_guardia(mapa, verbose)

    def es_bucle(x0, y0, mapa) -> bool:
        """ Verificar si el guardia está en un bucle. """
    
        vprint(verbose, f'x0 = {x0}, y0 = {y0}')
        x, y = x0, y0
        # Guardamos tuplas de (x, y, orientacion)
        posiciones = []
        while guardia_dentro_mapa(x, y, mapa):
            orientacion = mapa[y][x]
            estado = (x, y, orientacion)
            if estado in posiciones:
                return True
            posiciones.append(estado)
            x, y = mover_guardia(x, y, mapa)
        return False

    # Añadir obstáculos en las posiciones posibles
    for y, fila in enumerate(mapa):
        print(f"fila = {y}/{num_filas}")
        for x, char in enumerate(fila):
            print(f"columna = {x}/{num_columnas}")
            # Restablecer el mapa original
            mapa = [fila[:] for fila in mapa_original]
            if char == '.':
                mapa[y][x] = '#'
                if es_bucle(x0, y0, mapa):
                    result += 1
                mapa[y][x] = '.'

            
    print(f'resultado dia 6 - 1 = "{result}"')
    return result

if __name__ == "__main__":
    # assert dia6_1("test6_1.txt", verbose=True) == 41, "Error se esperaba 41."
    # dia6_1("data6_1.txt", verbose=False)
    # assert dia6_2("test6_1.txt", verbose=True) == 6, "Error se esperaba 6."
    dia6_2("data6_1.txt", verbose=False)
