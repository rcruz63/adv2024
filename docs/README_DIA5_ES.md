# Día 5: **Cola de impresión**

Satisfechos con su búsqueda en Ceres, el escuadrón de eruditos sugiere continuar explorando los montones de papelería del sub-sótano 17.

El departamento de impresión del Polo Norte está más ocupado que nunca en estas fechas cercanas a la Navidad, y mientras los Historiadores continúan su búsqueda en esta instalación histórica, un elfo que opera una impresora muy familiar te hace señas.

El elfo parece reconocerte, porque no pierde tiempo explicándote que las nuevas actualizaciones del manual de seguridad del trineo no se imprimen correctamente. No actualizar los manuales de seguridad sería un desastre, así que ofreces tu ayuda.

Los protocolos de seguridad indican claramente que las nuevas páginas para los manuales deben imprimirse en un orden muy específico. La notación `X|Y` significa que, si tanto la página `X` como la página `Y` deben producirse como parte de una actualización, la página `X` debe imprimirse en algún momento **antes** que la página `Y`.

El elfo te proporciona tanto las reglas de orden de las páginas como las páginas que deben producirse en cada actualización (tu entrada del acertijo), pero no sabe si cada actualización tiene las páginas en el orden correcto.

Por ejemplo:

```text
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
```

```text
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```

La primera sección especifica las reglas de orden de las páginas, una por línea. La primera regla, `47|53`, significa que, si una actualización incluye tanto la página `47` como la página `53`, entonces la página `47` debe imprimirse en algún momento antes que la página `53`. (No es necesario que `47` esté inmediatamente antes de `53`; pueden haber otras páginas entre ellas).

La segunda sección especifica los números de página de cada actualización. Como la mayoría de los manuales de seguridad son diferentes, las páginas necesarias para las actualizaciones también son diferentes. La primera actualización, `75,47,61,53,29`, significa que la actualización consta de las páginas `75`, `47`, `61`, `53` y `29`.

Para que las impresoras funcionen lo antes posible, empieza identificando qué actualizaciones ya están en el orden correcto.

En el ejemplo anterior, la primera actualización (`75,47,61,53,29`) está en el orden correcto:

- `75` está correctamente en primer lugar porque hay reglas que colocan cada otra página después de ella: `75|47`, `75|61`, `75|53` y `75|29`.
- `47` está correctamente en segundo lugar porque `75` debe estar antes de ella (`75|47`) y todas las demás páginas deben estar después de ella según `47|61`, `47|53` y `47|29`.
- `61` está correctamente en el medio porque `75` y `47` están antes que ella (`75|61` y `47|61`) y `53` y `29` están después que ella (`61|53` y `61|29`).
- `53` está correctamente en cuarto lugar porque está antes de la página `29` (`53|29`).
- `29` es la única página que queda, y está correctamente en último lugar.

Dado que la primera actualización no incluye algunos números de página, se ignoran las reglas de orden que involucran esos números de página faltantes.

La segunda y tercera actualizaciones también están en el orden correcto según las reglas. Al igual que la primera actualización, tampoco incluyen todos los números de página, por lo que solo se aplican algunas de las reglas de orden dentro de cada actualización.

La cuarta actualización, `75,97,47,61,53`, no está en el orden correcto: imprimirá `75` antes de `97`, lo que viola la regla `97|75`.

La quinta actualización, `61,13,29`, tampoco está en el orden correcto, ya que rompe la regla `29|13`.

La última actualización, `97,13,75,29,47`, no está en el orden correcto porque viola varias reglas.

Por alguna razón, los elfos también necesitan saber el número de página central de cada actualización que se imprime. Como actualmente solo estás imprimiendo las actualizaciones correctamente ordenadas, tendrás que encontrar el número de página central de cada actualización correctamente ordenada. En el ejemplo anterior, las actualizaciones correctamente ordenadas son:

```
75,47,61,53,29
97,61,53,29,13
75,29,13
```

Estos tienen números de página centrales de `61`, `53` y `29`, respectivamente. Sumando estos números de página da como resultado **143**.

Por supuesto, tendrás que tener cuidado: la lista real de reglas de orden de las páginas es más grande y complicada que el ejemplo anterior.

Determina qué actualizaciones ya están en el orden correcto. ¿Qué obtienes si sumas el número de página central de esas actualizaciones correctamente ordenadas? `7074`

## Parte Dos

Mientras los elfos comienzan a imprimir las actualizaciones correctamente ordenadas, tienes un poco de tiempo para arreglar el resto de ellas.

Para cada una de las actualizaciones desordenadas, utiliza las reglas de orden de las páginas para colocar los números de página en el orden correcto. En el ejemplo anterior, estas son las tres actualizaciones desordenadas y sus ordenamientos correctos:

- `75,97,47,61,53` se convierte en `97,75,47,61,53`.
- `61,13,29` se convierte en `61,29,13`.
- `97,13,75,29,47` se convierte en `97,75,47,29,13`.

Después de tomar solo las actualizaciones desordenadas y ordenarlas correctamente, sus números de página centrales son `47`, `29` y `47`. Sumando estos números obtenemos **123**.

Encuentra las actualizaciones que no están en el orden correcto. ¿Qué obtienes si sumas los números de página centrales después de ordenar correctamente solo esas actualizaciones?
