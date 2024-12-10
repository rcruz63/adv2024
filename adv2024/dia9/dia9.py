import os
import time

def vprint(verbose, *args):
    if verbose:
        print(*args)

def reorganizar_archivos(archivos, bloques_vacios, verbose: bool = False):
    """ Recorriendo la lista de archivos de ultimo al primero, de ID mayor a ID menor, el ID 0 no se procesa,
        Se cambian cada uno de los elementos de la lista asociado al ID por los elementos de la lista de 
        bloques_vacios comenzando por el primero, y se eliminan de la lista de bloques_vacios"""
    for ID in sorted(archivos.keys(), reverse=True):
        if ID == 0:
            continue
        old = archivos[ID]
        for index, bloque in enumerate(old):
            vacio = bloques_vacios[0]
            if vacio < bloque:
                bloques_vacios.remove(vacio)
                bloques_vacios.append(bloque)
                bloques_vacios.sort()
                old[index] = vacio
        archivos[ID] = old
        vprint(verbose, archivos)
        vprint(verbose, bloques_vacios)
    return archivos

def reorganizar_archivos_2(archivos, bloques_vacios, verbose: bool = False):
    """ Recorriendo la lista de archivos de último al primero, de ID mayor a ID menor, el ID 0 no se procesa,
        Se busca el mayor hueco libre donde quepa y que esté más a la izquierda"""
    for ID in sorted(archivos.keys(), reverse=True):
        if ID == 0:
            continue
        archivo = archivos[ID]
        posicion_archivo = archivo[0]
        size_archivo = archivo[1]
        changed = False
        for hueco in [h for h in bloques_vacios if h[0] < posicion_archivo]:
            posicion_hueco = hueco[0]
            size_hueco = hueco[1]
            if size_archivo <= size_hueco:
                changed = True
                bloques_vacios.append([posicion_archivo, size_archivo])
                bloques_vacios.remove(hueco)
                archivo[0] = posicion_hueco
                if size_archivo < size_hueco:
                    bloques_vacios.append((posicion_hueco + size_archivo, size_hueco - size_archivo))
            # Reordenar la lista de bloques vacios
            if changed:
                bloques_vacios.sort(key=lambda x: x[0])
                archivos[ID] = archivo
                break
        
        vprint(verbose, f'ID: {ID}, {archivos}')
        vprint(verbose, bloques_vacios)
    return archivos

def calcular_suma_de_comprobacion(archivos):
    """ Calcula la suma de comprobación del sistema de archivos """
    suma = 0
    for ID, bloques in archivos.items():
        for index, bloque in enumerate(bloques):
            suma += ID * bloque
    return suma

def calcular_suma_de_comprobacion_2(archivos):
    """ Calcula la suma de comprobación del sistema de archivos """
    suma = 0
    for ID, bloque in archivos.items():
        for i in range(bloque[0], bloque[0] + bloque[1]):
            suma += ID * i
    return suma

def dia9_1(data, verbose: bool = False):
    """ Función principal del día 9-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Procesar cada caracter del archivo
        archivo = True
        posicion = 0
        ID = 0
        archivos = {}
        # la lista bloques vacios debe ser una cola FIFO
        bloques_vacios = []
        for caracter in file.read():
            num = int(caracter)
            if archivo:
                # Generar una lista de numeros consecutivos a partir del valor de posicion (incluido) y del tamaño de num
                archivos[ID] = [posicion + i for i in range(num)]
                ID += 1
            else:
                bloques_vacios.extend([posicion + i for i in range(num)])
            posicion += num
            archivo = not archivo
    
    vprint(verbose, archivos)
    vprint(verbose, bloques_vacios)

    archivos = reorganizar_archivos(archivos, bloques_vacios, verbose)

    vprint(verbose, archivos)
    vprint(verbose, bloques_vacios)
    # Imprimir el resultado
    
    result = calcular_suma_de_comprobacion(archivos)
    print(f'resultado dia 9 - 1 = "{result}"')
    return result


def dia9_2(data, verbose: bool = False):
    """ Función principal del día 9-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Procesar cada caracter del archivo
        archivo = True
        posicion = 0
        ID = 0
        archivos = {}
        # la lista bloques vacios debe ser una cola FIFO
        bloques_vacios = []
        for caracter in file.read():
            num = int(caracter)
            if archivo:
                # Generar una lista de numeros consecutivos a partir del valor de posicion (incluido) y del tamaño de num
                archivos[ID] = [posicion, num]
                ID += 1
            else:
                if num > 0:
                    bloques_vacios.append([posicion, num])
            posicion += num
            archivo = not archivo
    
    vprint(verbose, archivos)
    vprint(verbose, bloques_vacios)

    archivos = reorganizar_archivos_2(archivos, bloques_vacios, verbose)

    vprint(verbose, archivos)
    vprint(verbose, bloques_vacios)
    # Imprimir el resultado
    
    result = calcular_suma_de_comprobacion_2(archivos)

    print(f'resultado dia 9 - 2 = "{result}"')
    return result

if __name__ == "__main__":
    start_time = time.time()
    # assert dia9_1("test9_1.txt", verbose=True) == 1928, "Error se esperaba 1928."
    # dia9_1("data9_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 1: {end_time - start_time:.4f} segundos")
    start_time = time.time()
    # assert dia9_2("test9_1.txt", verbose=True) == 2858, "Error se esperaba 2858."
    dia9_2("data9_1.txt", verbose=False)
    end_time = time.time()
    print(f"Tiempo de ejecución parte 2: {end_time - start_time:.4f} segundos")

