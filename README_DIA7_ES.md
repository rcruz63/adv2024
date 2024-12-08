# --- Día 7: Reparación del Puente ---
Los Historiadores te llevan a un puente de cuerdas familiar sobre un río en medio de la selva. El Jefe no está en este lado del puente; ¿quizás está al otro lado?

Cuando vas a cruzar el puente, notas un grupo de ingenieros intentando repararlo. (Aparentemente, se rompe con bastante frecuencia.) No podrás cruzar hasta que esté arreglado.

Preguntas cuánto tiempo llevará; los ingenieros te dicen que solo necesita calibraciones finales, pero ¡unos elefantes jóvenes estaban jugando cerca y `robaron todos los operadores` de sus ecuaciones de calibración! Podrían terminar las calibraciones si tan solo alguien pudiera determinar qué valores de prueba podrían producirse colocando cualquier combinación de operadores en sus ecuaciones de calibración (tu entrada del puzzle).

Por ejemplo:

```text
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

Cada línea representa una única ecuación. El valor de prueba aparece antes de los dos puntos en cada línea; tu trabajo es determinar si los números restantes pueden combinarse con operadores para producir el valor de prueba.

Los operadores siempre se evalúan `de izquierda a derecha`, no según las reglas de precedencia. Además, los números en las ecuaciones no se pueden reorganizar. Mirando hacia la selva, puedes ver elefantes sosteniendo dos tipos diferentes de operadores: `suma (+)` y `multiplicación (*)`.

Solo tres de las ecuaciones anteriores pueden hacerse verdaderas insertando operadores:

- `190: 10 19` tiene solo una posición que acepta un operador: entre `10 y 19`. Elegir `+` daría `29`, pero elegir `*` daría el valor de prueba `(10 * 19 = 190)`.
- `3267: 81 40 27` tiene dos posiciones para operadores. De las cuatro configuraciones posibles de operadores, dos hacen que el lado derecho coincida con el valor de prueba: ¡tanto `81 + 40 * 27` como `81 * 40 + 27` son iguales a 3267 (cuando se evalúan de izquierda a derecha)!
- `292: 11 6 16 20` se puede resolver de exactamente una manera: `11 + 6 * 16 + 20`.

Los ingenieros solo necesitan el resultado total de calibración, que es la suma de los valores de prueba de solo las ecuaciones que podrían ser verdaderas. En el ejemplo anterior, la suma de los valores de prueba para las tres ecuaciones listadas es 3749.

Determina qué ecuaciones podrían ser verdaderas. ¿Cuál es su resultado total de calibración? 
`1399219271639`

## --- Part Two ---
Los ingenieros parecen preocupados; el resultado total de calibración que le diste a ellos no está dentro de las tolerancias de seguridad. Justo entonces, te das cuenta de tu error: algunos elefantes bien escondidos están escondiendo un tercer tipo de operador.

El operador de concatenación (`||`) combina los dígitos de sus entradas izquierda y derecha en un solo número. Por ejemplo, 12 || 345 se convertiría en 12345. Todos los operadores se evalúan de izquierda a derecha.

Ahora, aparte de las tres ecuaciones que podrían hacerse verdaderas utilizando solo suma y multiplicación, el ejemplo anterior tiene tres ecuaciones más que pueden hacerse verdaderas insertando operadores:

- 156: 15 6 puede hacerse verdadero a través de una sola concatenación: 15 || 6 = 156.
- 7290: 6 8 6 15 puede hacerse verdadero usando 6 * 8 || 6 * 15.
- 192: 17 8 14 puede hacerse verdadero usando 17 || 8 + 14.

Sumando todos los valores de prueba (los tres que se podían hacer antes de usar solo + y * más los tres nuevos que ahora se pueden hacer insertando también ||) se obtiene el nuevo resultado total de calibración de `11387`.

Usando tu nueva comprensión de los escondites de los elefantes, determina qué ecuaciones podrían ser verdaderas. ¿Cuál es su resultado total de calibración?
`275791737999003`
