# --- Día 3: Reflexión ---
"¡Nuestros ordenadores están teniendo problemas, así que no tengo ni idea de si tenemos algún Historiador Jefe en stock! Puedes revisar el almacén, si quieres," dice el ligeramente alterado dependiente de la Tienda de Alquiler de Trineos del Polo Norte. Los Historiadores salen a echar un vistazo.

El dependiente se vuelve hacia ti. "¿Hay alguna posibilidad de que puedas ver por qué nuestros ordenadores están teniendo problemas de nuevo?"

El ordenador parece estar intentando ejecutar un programa, pero su memoria (tu entrada del rompecabezas) está corrupta. ¡Todas las instrucciones se han mezclado!

Parece que el objetivo del programa es simplemente multiplicar algunos números. Lo hace con instrucciones como mul(X,Y), donde X e Y son cada uno números de 1 a 3 dígitos. Por ejemplo, mul(44,46) multiplica 44 por 46 para obtener un resultado de 2024. De manera similar, mul(123,4) multiplicaría 123 por 4.

Sin embargo, debido a que la memoria del programa está corrupta, también hay muchos caracteres inválidos que deben ser ignorados, incluso si parecen formar parte de una instrucción mul. Secuencias como mul(4*, mul(6,9!, ?(12,34), o mul ( 2 , 4 ) no hacen nada.

Por ejemplo, considera la siguiente sección de memoria corrupta:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Solo las cuatro secciones resaltadas son instrucciones mul reales. Sumando el resultado de cada instrucción se obtiene 161 (2*4 + 5*5 + 11*8 + 8*5).

Escanea la memoria corrupta en busca de instrucciones mul no corruptas. ¿Qué obtienes si sumas todos los resultados de las multiplicaciones? `183380722`

## Parte Dos
Mientras escaneas la memoria corrupta, notas que algunas de las declaraciones condicionales también están intactas. Si manejas algunas de las declaraciones condicionales no corruptas del programa, podrías obtener un resultado aún más preciso.

Hay dos nuevas instrucciones que tendrás que manejar:

La instrucción do() habilita las instrucciones mul futuras.
La instrucción don't() deshabilita las instrucciones mul futuras.
Solo se aplica la instrucción do() o don't() más reciente. Al inicio del programa, las instrucciones mul están habilitadas.

Por ejemplo:

```scss
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
```

Esta memoria corrupta es similar al ejemplo anterior, pero esta vez las instrucciones mul(5,5) y mul(11,8) están deshabilitadas porque hay una instrucción don't() antes de ellas. Las demás instrucciones mul funcionan con normalidad, incluyendo la última, que se vuelve a habilitar gracias a una instrucción do().

Esta vez, la suma de los resultados es 48 (2*4 + 8*5)

Maneja las nuevas instrucciones. ¿Cuál es la suma de los resultados de solo las multiplicaciones habilitadas?