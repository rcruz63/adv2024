# --- Día 11: Guijarros Plutonianos ---
La antigua civilización de Plutón era conocida por su capacidad para manipular el espacio-tiempo, y mientras Los Historiadores exploran sus corredores infinitos, has notado un extraño conjunto de piedras que desafían la física.

A primera vista, parecen piedras normales: están dispuestas en una línea perfectamente recta, y cada piedra tiene un número grabado.

Lo extraño es que cada vez que parpadeas, las piedras cambian.

A veces, el número grabado en una piedra cambia. Otras veces, una piedra puede dividirse en dos, haciendo que todas las demás piedras se desplacen un poco para hacer espacio en su línea perfectamente recta.

Al observarlas durante un tiempo, descubres que las piedras tienen un comportamiento consistente. Cada vez que parpadeas, las piedras cambian simultáneamente según la primera regla aplicable de esta lista:

- Si la piedra tiene grabado el número 0, es reemplazada por una piedra con el número 1 grabado.
- Si la piedra tiene grabado un número que tiene una cantidad par de dígitos, es reemplazada por dos piedras. La mitad izquierda de los dígitos se graba en la nueva piedra izquierda, y la mitad derecha de los dígitos se graba en la nueva piedra derecha. (Los nuevos números no mantienen ceros a la izquierda extras: 1000 se convertiría en piedras 10 y 0.)
- Si ninguna de las otras reglas se aplica, la piedra es reemplazada por una nueva piedra; el número de la piedra antigua multiplicado por 2024 se graba en la nueva piedra.
Sin importar cómo cambien las piedras, su orden se preserva, y permanecen en su línea perfectamente recta.

¿Cómo evolucionarán las piedras si sigues parpadeando? Tomas nota del número grabado en cada piedra de la línea (tu input del puzzle).

Si tienes un arreglo de cinco piedras grabadas con los números `0 1 10 99 999` y parpadeas una vez, las piedras se transforman así:

- La primera piedra, 0, se convierte en una piedra marcada con 1.
- La segunda piedra, 1, se multiplica por 2024 para convertirse en 2024.
- La tercera piedra, 10, se divide en una piedra marcada con 1 seguida de una piedra marcada con 0.
- La cuarta piedra, 99, se divide en dos piedras marcadas con 9.
- La quinta piedra, 999, es reemplazada por una piedra marcada con 2021976.

Así, después de parpadear una vez, tus cinco piedras se convertirían en un arreglo de siete piedras grabadas con los números `1 2024 1 0 9 9 2021976`.

Aquí hay un ejemplo más largo:

    Arreglo inicial:
    125 17

    Después de 1 parpadeo:
    253000 1 7

    Después de 2 parpadeos:
    253 0 2024 14168

    Después de 3 parpadeos:
    512072 1 20 24 28676032

    Después de 4 parpadeos:
    512 72 2024 2 0 2 4 2867 6032

    Después de 5 parpadeos:
    1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

    Después de 6 parpadeos:
    2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

En este ejemplo, después de parpadear seis veces, tendrías 22 piedras. ¡Después de parpadear 25 veces, tendrías `55312` piedras!

Considera el arreglo de piedras frente a ti. ¿Cuántas piedras tendrás después de parpadear 25 veces?

`184927`

--- Part Two ---
Los Historadores están tomando mucho tiempo. Para ser justos, los corredores infinitos son muy grandes.

¿Cuántas piedras tendrías después de parpadear un total de 75 veces?
