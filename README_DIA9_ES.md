# --- Día 9: Fragmentador de disco ---
¡Otro empujón del botón te deja en los familiares pasillos de algunos anfípodos amistosos! Menos mal que cada uno consiguió de alguna manera su propio mini submarino. Los Historiadores salen disparados en busca del Jefe, principalmente chocándose directamente contra las paredes.

Mientras Los Historiadores rápidamente averiguan cómo pilotar estas cosas, te fijas en un anfípodo en la esquina que está teniendo problemas con su ordenador. Está intentando crear más espacio libre contiguo compactando todos los archivos, pero su programa no funciona; te ofreces a ayudar.

Te muestra el mapa del disco (tu entrada del puzzle) que ya ha generado. Por ejemplo:

    2333133121414131402
El mapa del disco utiliza un formato denso para representar la disposición de archivos y espacio libre en el disco. Los dígitos alternan entre indicar la longitud de un archivo y la longitud del espacio libre.

Así, un mapa de disco como 12345 representaría un archivo de un bloque, dos bloques de espacio libre, un archivo de tres bloques, cuatro bloques de espacio libre y luego un archivo de cinco bloques. Un mapa de disco como 90909 representaría tres archivos de nueve bloques en fila (sin espacio libre entre ellos).

Cada archivo en el disco también tiene un número ID basado en el orden de los archivos tal como aparecen antes de ser reordenados, empezando con el ID 0. Así, el mapa de disco 12345 tiene tres archivos: un archivo de un bloque con ID 0, un archivo de tres bloques con ID 1 y un archivo de cinco bloques con ID 2. Usando un carácter para cada bloque donde los dígitos son el ID del archivo y . es espacio libre, el mapa de disco 12345 representa estos bloques individuales:

    0..111....22222
El primer ejemplo anterior, 2333133121414131402, representa estos bloques individuales:

    00...111...2...333.44.5555.6666.777.888899
El anfípodo querría mover los bloques de archivo uno a uno desde el final del disco hasta el bloque de espacio libre más a la izquierda (hasta que no queden huecos entre los bloques de archivo). Para el mapa de disco 12345, el proceso se ve así:

    0..111....22222
    02.111....2222.
    022111....222..
    0221112...22...
    02211122..2....
    022111222......
El primer ejemplo requiere algunos pasos más:

    00...111...2...333.44.5555.6666.777.888899
    009..111...2...333.44.5555.6666.777.88889.
    0099.111...2...333.44.5555.6666.777.8888..
    00998111...2...333.44.5555.6666.777.888...
    0099811188.2...333.44.5555.6666.777.8.....
    009981118882...333.44.5555.6666.777.......
    0099811188827..333.44.5555.6666.77........
    00998111888277.333.44.5555.6666.7.........
    009981118882777333.44.5555.6666...........
    009981118882777333644.5555.666............
    00998111888277733364465555.66.............
    0099811188827773336446555566..............

El paso final de este proceso de compactación de archivos es actualizar la suma de comprobación del sistema de archivos. Para calcular la suma de comprobación, suma el resultado de multiplicar la posición de cada uno de estos bloques por el número ID del archivo que contiene. El bloque más a la izquierda está en la posición 0. Si un bloque contiene espacio libre, sáltalo.

Continuando con el primer ejemplo, los primeros bloques multiplicados por su número ID de archivo son 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, y así sucesivamente. En este ejemplo, la suma de comprobación es la suma de todos estos, 1928.

Compacta el disco duro del anfípodo usando el proceso que ha solicitado. ¿Cuál es la suma de comprobación del sistema de archivos resultante? (Ten cuidado al copiar/pegar la entrada para este puzzle; es una única línea muy larga.)

`6341711060162`

## --- Parte Dos ---
Al completar, dos cosas quedan inmediatamente claras. Primero, el disco definitivamente tiene mucho más espacio libre contiguo, justo como esperaba el anfípodo. Segundo, ¡la computadora está funcionando mucho más lento! ¿Quizás introducir toda esa fragmentación del sistema de archivos fue una mala idea?

El ansioso anfípodo ya tiene un nuevo plan: en lugar de mover bloques individuales, le gustaría intentar compactar los archivos en su disco moviendo archivos completos.

Esta vez, intenta mover archivos completos al tramo de bloques de espacio libre más a la izquierda que pueda contener el archivo. Intenta mover cada archivo exactamente una vez en orden decreciente de número ID de archivo, comenzando con el archivo que tiene el número ID más alto. Si no hay un tramo de espacio libre a la izquierda de un archivo que sea lo suficientemente grande para contenerlo, el archivo no se mueve.

El primer ejemplo de arriba ahora procede de manera diferente:

    00...111...2...333.44.5555.6666.777.888899
    0099.111...2...333.44.5555.6666.777.8888..
    0099.1117772...333.44.5555.6666.....8888..
    0099.111777244.333....5555.6666.....8888..
    00992111777.44.333....5555.6666.....8888..

El proceso de actualización de la suma de comprobación del sistema de archivos es el mismo; ahora, la suma de comprobación de este ejemplo sería 2858.

Empieza de nuevo, ahora compactando el disco duro del anfípodo usando este nuevo método. ¿Cuál es la suma de comprobación del sistema de archivos resultante?