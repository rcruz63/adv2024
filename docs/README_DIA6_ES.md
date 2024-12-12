# --- Día 6: La Patrulla del Guardián ---
Los Historiadores usan de nuevo su aparato sofisticado, esta vez para transportaros a todos al prototipo de laboratorio de fabricación de trajes en el Polo Norte... ¡en el año 1518! Resulta que tener acceso directo a la historia es muy conveniente para un grupo de historiadores.

Aún así, hay que tener cuidado con las paradojas temporales, así que será importante evitar encontrarse con cualquier persona de 1518 mientras Los Historiadores buscan al Jefe. Por desgracia, un solo guardia está patrullando esta parte del laboratorio.

¿Quizás puedas averiguar adónde irá el guardia con antelación para que Los Historiadores puedan buscar con seguridad?

Empiezas haciendo un mapa (tu entrada del puzzle) de la situación. Por ejemplo:

```text
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

El mapa muestra la posición actual del guardia con un ^ (para indicar que el guardia está actualmente mirando hacia arriba desde la perspectiva del mapa). Cualquier obstáculo - cajas, escritorios, reactores alquímicos, etc. - se representan con #.

Los guardias de laboratorio en 1518 siguen un protocolo de patrulla muy estricto que implica repetir estos pasos:

- Si hay algo directamente delante de ti, gira 90 grados a la derecha.
- De lo contrario, avanza un paso hacia adelante.

Siguiendo el protocolo anterior, el guardia se mueve hacia arriba varias veces hasta que se topa con un obstáculo (en este caso, una pila de prototipos de trajes fallidos):

```text
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Como ahora hay un obstáculo frente al guardia, este gira a la derecha antes de continuar recto en su nueva dirección:

```text
....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Al encontrarse con otro obstáculo (una bobina de polímeros muy largos), gira a la derecha otra vez y continúa hacia abajo:

```text
....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
```

Este proceso continúa durante un tiempo, pero el guardia finalmente abandona el área mapeada (después de pasar al lado de un tanque de solvente universal):

```text
....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
```

Al predecir la ruta del guardia, puedes determinar qué posiciones específicas del laboratorio estarán en la ruta de la patrulla. Incluyendo la posición inicial del guardia, las posiciones visitadas por el guardia antes de salir del área se marcan con una X:

```text
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
```

En este ejemplo, el guardia visitará 41 posiciones distintas en tu mapa.

Predice la trayectoria del guardia. ¿Cuántas posiciones distintas visitará el guardia antes de salir del área? `4988`

## --- Parte Dos ---
Mientras Los Historiadores comienzan a trabajar alrededor de la ruta de patrulla del guardia, tomas prestado su aparato y sales del laboratorio. Desde la seguridad de un armario de suministros, viajas en el tiempo durante los últimos meses y registras cada noche el estado del puesto de guardia del laboratorio en las paredes del armario.

Cuando regresas, después de lo que parece sólo unos segundos para Los Historiadores, ellos explican que el área de patrulla del guardia es simplemente demasiado grande para que puedan registrar el laboratorio sin ser descubiertos.

Afortunadamente, están bastante seguros de que añadir un solo nuevo obstáculo no provocará una paradoja temporal. Les gustaría colocar el nuevo obstáculo de tal manera que el guardia quede atrapado en un bucle, dejando el resto del laboratorio seguro para su búsqueda.

Para tener la menor probabilidad de crear una paradoja temporal, Los Historiadores quieren conocer todas las posibles posiciones para dicho obstáculo. El nuevo obstáculo no puede colocarse en la posición inicial del guardia: el guardia está allí ahora y se daría cuenta.

En el ejemplo anterior, sólo hay 6 posiciones diferentes donde un nuevo obstáculo causaría que el guardia quedase atrapado en un bucle. Los diagramas de estas seis situaciones usan O para marcar el nuevo obstáculo, | para mostrar una posición en la que el guardia se mueve arriba/abajo, - para mostrar una posición donde el guardia se mueve izquierda/derecha, y + para mostrar una posición donde el guardia se mueve tanto arriba/abajo como izquierda/derecha.

Opción uno, poner una imprenta junto a la posición inicial del guardia:

```text
....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
```

Opción dos, poner una pila de prototipos de trajes fallidos en el cuadrante inferior derecho del área mapeada:

```text
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
```

Opción tres, poner una caja de tela para prototipos de chimeneas ajustadas junto al escritorio alto en el cuadrante inferior derecho:

```text
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
```

Opción cuatro, poner un retroencabulador alquímico cerca de la esquina inferior izquierda:

```text
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
```

Opción cinco, poner el retroencabulador alquímico un poco más a la derecha:

```text
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
```

Opción seis, poner un tanque de pegamento soberano justo al lado del tanque de solvente universal:

```text
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
```

Realmente no importa qué elijas usar como obstáculo, siempre que tú y Los Historiadores podáis colocarlo sin que el guardia lo note. Lo importante es tener suficientes opciones para encontrar una que minimice las paradojas temporales, y en este ejemplo, hay 6 posiciones diferentes donde podrías elegir.

Necesitas hacer que el guardia se quede atrapado en un bucle añadiendo un único nuevo obstáculo. ¿Cuántas posiciones diferentes podrías elegir para este obstáculo? `1697`
