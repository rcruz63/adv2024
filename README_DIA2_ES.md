# Día 2: Informes Nariz Roja
Por suerte, la primera ubicación que los historiadores quieren buscar no está muy lejos de la oficina del Historiador Jefe.

Aunque en la planta de fusión/fisión nuclear Nariz Roja no parece haber ningún rastro del Historiador Jefe, los ingenieros corren hacia ti tan pronto como te ven. Al parecer, aún hablan de la vez que Rudolph fue salvado mediante síntesis molecular a partir de un solo electrón.

Rápidamente añaden que, ya que estás aquí, les vendría muy bien tu ayuda para analizar unos datos inusuales procedentes del reactor Nariz Roja. Te giras para comprobar si los historiadores están esperando, pero parece que ya se han dividido en grupos y están buscando en cada rincón de la instalación. Así que decides ofrecer tu ayuda con los datos inusuales.

Los datos inusuales (tu entrada del acertijo) consisten en muchos informes, uno por línea. Cada informe es una lista de números, llamados niveles, separados por espacios. Por ejemplo:

```text
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

Estos datos de ejemplo contienen seis informes, cada uno con cinco niveles.

Los ingenieros están tratando de averiguar cuáles informes son seguros. Los sistemas de seguridad del reactor Nariz Roja solo toleran niveles que sean gradualmente crecientes o gradualmente decrecientes. Por lo tanto, un informe se considera seguro únicamente si se cumplen las dos condiciones siguientes:

Los niveles son todos crecientes o todos decrecientes.
La diferencia entre dos niveles consecutivos es al menos 1 y como máximo 3.
En el ejemplo anterior, los informes pueden evaluarse como seguros o inseguros siguiendo estas reglas:

7 6 4 2 1: Seguro, porque los niveles son todos decrecientes y las diferencias son de 1 o 2.
1 2 7 8 9: Inseguro, porque entre 2 y 7 hay un aumento de 5.
9 7 6 2 1: Inseguro, porque entre 6 y 2 hay una disminución de 4.
1 3 2 4 5: Inseguro, porque 1 3 es creciente, pero 3 2 es decreciente.
8 6 4 4 1: Inseguro, porque 4 4 no es ni creciente ni decreciente.
1 3 6 7 9: Seguro, porque los niveles son todos crecientes y las diferencias son de 1, 2 o 3.
En este ejemplo, 2 informes son seguros.

Analiza los datos inusuales proporcionados por los ingenieros. ¿Cuántos informes son seguros? `402``

## Parte Dos
Los ingenieros están sorprendidos por el bajo número de informes seguros hasta que se dan cuenta de que olvidaron hablarte del Amortiguador de Problemas.

El Amortiguador de Problemas es un módulo instalado en el reactor que permite a los sistemas de seguridad del reactor tolerar un único nivel problemático en lo que de otro modo sería un informe seguro. ¡Es como si ese nivel problemático nunca hubiera existido!

Ahora, se aplican las mismas reglas que antes, excepto que si eliminando un único nivel de un informe inseguro este se convierte en seguro, entonces dicho informe se considera seguro.

Con esta nueva regla, más informes del ejemplo anterior son ahora seguros:

7 6 4 2 1: Seguro, sin necesidad de eliminar ningún nivel.
1 2 7 8 9: Inseguro, sin importar qué nivel se elimine.
9 7 6 2 1: Inseguro, sin importar qué nivel se elimine.
1 3 2 4 5: Seguro, eliminando el segundo nivel (3).
8 6 4 4 1: Seguro, eliminando el tercer nivel (4).
1 3 6 7 9: Seguro, sin necesidad de eliminar ningún nivel.
Gracias al Amortiguador de Problemas, ahora 4 informes son seguros.

Actualiza tu análisis para incluir situaciones en las que el Amortiguador de Problemas pueda eliminar un único nivel de los informes inseguros. ¿Cuántos informes son ahora seguros?