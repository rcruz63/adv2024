# Día 1: La histeria del historiador
El Historiador Jefe siempre está presente en el gran lanzamiento del trineo de Navidad, ¡pero nadie lo ha visto en meses! Lo último que se supo de él es que estaba visitando lugares históricamente significativos para el Polo Norte. Un grupo de historiadores sénior te ha pedido que los acompañes mientras inspeccionan los lugares donde creen que es más probable que haya estado.

A medida que verifican cada lugar, lo marcarán en su lista con una estrella. Creen que el Historiador Jefe debe estar en uno de los primeros cincuenta lugares que planean buscar, así que, para salvar la Navidad, necesitas ayudarlos a conseguir cincuenta estrellas en su lista antes de que Papá Noel despegue el 25 de diciembre.

Recoge estrellas resolviendo acertijos. Cada día del calendario de Adviento se desbloquearán dos acertijos; el segundo se desbloquea al completar el primero. Cada acertijo concede una estrella. ¡Buena suerte!

Ni siquiera has salido todavía, y el grupo de historiadores sénior elfos ya se ha topado con un problema: su lista de lugares para inspeccionar está completamente vacía. Finalmente, alguien decide que el mejor lugar para buscar primero sería la oficina del Historiador Jefe.

Al entrar en la oficina, todos confirman que, efectivamente, el Historiador Jefe no está. Sin embargo, los elfos encuentran una colección de notas y listas de lugares históricamente significativos. Parece que estas notas son parte de la planificación que el Historiador Jefe estaba haciendo antes de desaparecer. ¿Quizás estas notas puedan servir para determinar qué lugares buscar?

Por toda la oficina del Historiador Jefe, los lugares históricamente significativos no están listados por nombre, sino por un número único llamado ID de ubicación. Para asegurarse de no pasar nada por alto, los historiadores se dividen en dos grupos, cada uno buscando en la oficina y tratando de crear su propia lista completa de IDs de ubicación.

Hay solo un problema: al comparar las dos listas una al lado de la otra (tu entrada del acertijo), rápidamente queda claro que las listas no son muy similares. ¿Puedes ayudar a los historiadores a reconciliar sus listas?

Por ejemplo:

```text
3   4
4   3
2   5
1   3
3   9
3   3
```

Tal vez las listas solo difieran por una pequeña cantidad. Para averiguarlo, empareja los números y mide cuán diferentes son. Empareja el número más pequeño de la lista izquierda con el más pequeño de la lista derecha, luego el segundo más pequeño de la izquierda con el segundo más pequeño de la derecha, y así sucesivamente.

En cada par, calcula la diferencia entre los dos números; tendrás que sumar todas esas diferencias. Por ejemplo, si emparejas un 3 de la lista izquierda con un 7 de la lista derecha, la diferencia es 4; si emparejas un 9 con un 3, la diferencia es 6.

En la lista de ejemplo anterior, los pares y las diferencias serían los siguientes:

- El número más pequeño en la lista izquierda es 1, y el número más pequeño en la lista derecha es 3. La diferencia entre ellos es 2.
- El segundo número más pequeño en la lista izquierda es 2, y el segundo más pequeño en la lista derecha es otro 3. La diferencia entre ellos es 1.
- El tercer número más pequeño en ambas listas es 3, así que la diferencia entre ellos es 0.
- Los siguientes números para emparejar son 3 y 4, con una diferencia de 1.
- Los quintos números más pequeños en cada lista son 3 y 5, con una diferencia de 2.
- Finalmente, el número más grande en la lista izquierda es 4, mientras que el más grande en la lista derecha es 9; estos tienen una diferencia de 5.

Para encontrar la distancia total entre la lista izquierda y la lista derecha, suma las diferencias entre todos los pares que encontraste. En el ejemplo anterior, esto es 2 + 1 + 0 + 1 + 2 + 5, una distancia total de 11.

Tus listas reales (izquierda y derecha) contienen muchos IDs de ubicación. ¿Cuál es la distancia total entre tus listas?