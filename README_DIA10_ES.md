# ESPAÑOL
# --- Día 10: A Pata ---
Todos llegan a una Instalación de Producción de Lava en una isla flotante en el cielo. Mientras los demás comienzan a buscar en el enorme complejo industrial, sientes un pequeño hocico que te toca la pierna y miras hacia abajo para descubrir un reno con un casco de seguridad.

El reno sostiene un libro titulado "Guía de Senderismo de la Isla de Lava". Sin embargo, cuando abres el libro, descubres que la mayor parte parece haber sido quemada por la lava. Justo cuando estás a punto de preguntar cómo puedes ayudar, el reno te trae un mapa topográfico en blanco del área circundante (tu entrada del rompecabezas) y te mira emocionado.

¿Quizás puedas ayudar a completar los senderos de senderismo faltantes?

El mapa topográfico indica la altura en cada posición usando una escala de 0 (la más baja) a 9 (la más alta). Por ejemplo:

    0123
    1234
    8765
    9876

Basado en fragmentos no quemados del libro, determinas que un buen sendero de senderismo es lo más largo posible y tiene una pendiente gradual y uniforme. Para todos los propósitos prácticos, esto significa que un sendero de senderismo es cualquier camino que comienza en la altura 0, termina en la altura 9 y siempre aumenta en una altura de exactamente 1 en cada paso. Los senderos de senderismo nunca incluyen pasos diagonales, solo hacia arriba, abajo, izquierda o derecha (desde la perspectiva del mapa).

Levantas la vista del mapa y notas que el reno ha comenzado a construir una pequeña pila de lápices, marcadores, reglas, compases, pegatinas y otros equipos que podrías necesitar para actualizar el mapa con senderos de senderismo.

Un punto de partida es cualquier posición que comienza uno o más senderos de senderismo; aquí, estas posiciones siempre tendrán altura 0. Reuniendo más fragmentos de páginas, estableces que la puntuación de un punto de partida es el número de posiciones de altura 9 alcanzables desde ese punto de partida a través de un sendero de senderismo. En el ejemplo anterior, el único punto de partida en la esquina superior izquierda tiene una puntuación de 1 porque puede alcanzar un solo 9 (el de la esquina inferior izquierda).

Este punto de partida tiene una puntuación de 2:

    ...0...
    ...1...
    ...2...
    6543456
    7.....7
    8.....8
    9.....9

(Las posiciones marcadas con . son casillas intransitables para simplificar estos ejemplos; no aparecen en tu mapa topográfico real).

Este punto de partida tiene una puntuación de 4 porque cada 9 es alcanzable a través de un sendero de senderismo excepto el que está inmediatamente a la izquierda del punto de partida:

    ..90..9
    ...1.98
    ...2..7
    6543456
    765.987
    876....
    987....

Este mapa topográfico contiene dos puntos de partida; el punto de partida en la parte superior tiene una puntuación de 1, mientras que el punto de partida en la parte inferior tiene una puntuación de 2:

    10..9..
    2...8..
    3...7..
    4567654
    ...8..3
    ...9..2
    .....01

Aquí hay un ejemplo más grande:

    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732

Este ejemplo más grande tiene 9 puntos de partida. Considerando los puntos de partida en orden de lectura, tienen puntuaciones de 5, 6, 5, 3, 1, 3, 5, 3 y 5. Sumando estas puntuaciones, la suma de las puntuaciones de todos los puntos de partida es 36.

El reno alegremente lleva un transportador y lo añade a la pila. ¿Cuál es la suma de las puntuaciones de todos los puntos de partida en tu mapa topográfico?