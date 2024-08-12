---
title: Otra manera de entender D'Hondt
date: 2024-06-09 09:03
author: David García Garzón
tags: D'Hondt
status: published
cover: images/dhondt-seat-rest-view.png
---

<!-- PELICAN_BEGIN_SUMMARY -->

D'Hondt es el método de reparto de escaños que se usa, por ejemplo, en España para cada circunscripción.
A menudo se nos explica como procedimiento,
pero ¿qué pretende obtener?
La respuesta a esta pregunta nos empoderará para entender
sus efectos y el efecto real de nuestro voto
y nos servirá como herramienta para desmontar muchos mitos.

<!-- PELICAN_END_SUMMARY -->


## El procedimiento

Cuando se nos explica el método de D'Hondt
que usamos para repartir los escaños en una circunscripción,
se nos suele explicar un procedimiento.
(No hace falta que lo leas, lo voy a simplificar después)

> Para cada candidatura X, se calcula el cociente $V_X \over S_X + 1$
> donde $V_X$ son los votos obtenidos por esa candidatura
> y $S_X$ los escaños que le han sido repartidos hasta el momento, inicialmente 0.
> Se asigna escaño a la candidatura con el cociente más alto,
> se le recalcula su cociente
> y se repite hasta que todos los escaños se han repartido.

Este procedimiento tiene un punto de complejidad para reducir el número de cocientes a calcular,
lo que es de agradecir si tenemos que hacerlo a mano.
Pero, hoy en día, tenemos ordenadores.
Al final lo que estamos haciendo es:

> Otorgar escaño a los mayores cocientes resultantes de
> dividir los votos de cada candidatura
> por sucesivos enteros 1, 2, 3...

Lo que mostramos en esta tabla en el simulador:

![Cocientes de un reparto de D'Hondt real.
Cada celda de la tabla contiene los votos obtenidos por cada candidatura dividido por un número de escaños.
Los 33 mayores cocientes con el fondo azul fueron los que obtuvieron escaño,
](/images/revote-dhondttable.png)

Aún así, simplificando el procedimiento,
no explica porqué hacemos esto.
Entenderlo nos va a permitir entender mejor sus efectos.

Entonces, ¿cuál sería el objetivo?

## Una subasta inversa

El método de D'Hondt resuelve el problema de **encontrar un precio**
(cuántos votos ha de costar un escaño) para que
se **repartan exactamente** los escaños disponibles,
ni de más ni de menos.

Una candidatura que tenga 100.000 votos:

- No obtendrá representación si el precio es superior a 100.000
- Obtendrá un escaño cuando sea 100.000 (100.000/1) o inferior
- Obtendrá dos cuando sea 50.000 (100.000/2) o menor
- Obtendra tres cuando sea 33.333 (100.000/3) o menor
- ...

Eso es lo que representan los cocientes:
el precio máximo por el que cada candidatura puede obtener un cierto número de escaños.

Cuando el Método de D'Hondt va escogiendo cocientes ordenados de mayor a menor,
lo que está haciendo es ir bajando el precio hasta que se han escogido tantos cocientes
como escaños hay disponibles, asegurando el reparto exacto.
Le llamamos una subasta inversa porque, en vez de ir subiendo el precio,
lo bajamos hasta que casamos oferta con demanda.

Esta es la perspectiva del método de D'Hondt que nos va a permitir
llegar a un montón de conclusiones sobre como funciona el sistema electoral.

Vamos a escarbar un poco más.

## Escaños y restos

![
Fijado el precio del escaño cada barra està dividida
en tantos segmentos de ese tamaño como escaños obtenidos.
Al final, todas las barras tienen un segmento translucido más corto
que son los restos.
La tercera candidatura ha fijado el precio y no tiene restos.
](/images/dhondt-seat-rest-view.png)

Visualmente, tal y como muestra esta vista del simulador,
dado un precio $P$, los votos de cada candidatura
se dividirán en tantos bloques de tamaño $P$ como escaños obtenidos
y un bloque extra menor que $P$, representado translúcido al final de la barra,
que serían los restos que no han llegado a conseguir escaño.

El reparto sería *exacto* si los escaños repartidos a ese precio
coinciden con los escaños disponibles.

Más formalmente, D'Hondt nos sirve para encontrar un precio, $P$,
tal que, para cualquier candidatura X:

$$ V_X = S_X P + R_X $$

Donde:

- $V_X \in \mathbb{N}$ son los votos que ha obtenido X, tal que $V_{total} = \sum_{\forall X}{V_X}$
- $S_X \in \mathbb{N}$ son los escaños que consigue X del reparto,  tal que  $ S_{total} = \sum_{\forall X}{S_X}$
- $R_X \in \mathbb{R}$ son los restos que sobran de repartir a $P$ y se tiene que dar que $ 0 <= R_X < P$


## El último cociente con escaño, $P_{max}$

Llamemos C a la candidatura que ha obtenido el último escaño.
Su último cociente escogido, $P_C$, fijará el precio $P_{max}$,
que será el máximo con el que P obtiene exactamente $S_C$ escaños sin que le sobren votos.

$$ P_{max} = P_C = { V_C \over S_C }$$
$$R_C = 0$$

Si el preció fuera levemente superior, C no tendría suficientes votos para obtener $S_C$ escaños.
Al reparto le sobraría un escaño y ya no sería exacto.

En el simulador, este último cociente en entrar, se indica con los números en rojo y el fondo azul.
Es el menor de los marcados en azul que han obtenido escaño.

![](/images/trasvases-ejemplo-cociente-fijador.png)

## El primer cociente excluido, $P_{min}$

Al mayor cociente que se ha quedado sin representacion,
el inmediatamente inferior a $P_C$, le vamos a llamar $P_D$
y vamos a llamar D a la candidatura a la que pertenece.
Este cociente marca el precio que llamaremos $P_{min}$,
Repartir escaños a ese precio o menores nos haria repartir escaños de más.
En concreto, a ese precio repartiriamos $S_D+1$ escaños para D y
$S_{total} + 1$ en total.

$$ P_{min} = P_D = { V_D \over {S_D + 1}} $$

En el simulador, se indica en rojo también, pero con fondo blanco,
como el resto de cocientes sin escaño, de los cuales $P_D$ es el mayor de todos.

![](/images/trasvases-ejemplo-cociente-excluido.png)

Para precios superiores a $P_{min}$, el reparto aún sería exacto.
Es decir que el reparto exacto no se da para un precio concreto,
sinó para un intervalo de precios:

$$P_{min} < P <= P_{max}$$

La existencia de estos dos precios y sus dinámicas nos servirán
para entender, de forma mucho más simple,
los efectos de trasvases de votos entre candidaturas.

## Acotando y estimando el precio

Sabiendo que el objetivo de D'Hondt es
encontrar un precio que reparta los escaños exactamemte,
podemos experimentar con otras formas de encontrarlo.
Por ejemplo, podemos probar valores,
si sobran escaños bajamos el precio, si faltan lo subimos,
hasta que encontremos un precio que reparta exactamente los escaños,
uno entre $P_{min}$ y $P_{max}$.

Ademas, podemos acotar la búsqueda entre los siguientes dos casos extremos:

- la cota superior, para el caso en que a nadie le sobran votos:
$ P_H = {V_{total} \over S_{total}}$[^cotasuperior], y
- la cota inferior, para el caso en que a todos les falta un voto para el siguiente escaño
$ P_L = {V_{total} \over S_{total} + K }$[^cotainferior], donde $K$ es el número de candidaturas.

$$P_L <= P_{min} < P <= P_{max} <= P_H$$

[^cotasuperior]:
La cota superior $P_H$ viene de que, si no hay restos, $$V_{total} = S_{total} P_H$$
y entonces
$$P_H = { V_{total} \over S_{total}}$$


[^cotainferior]:
La cota inferior viene de que, si todos las candidaturas ($K$),
tienen los restos máximos (casi $P_L$), entonces:
$$V_{total} = S_{total} P_L + K P_L$$
y entonces
$$P_L = { V_{total}  \over S_{total} + K }$$

Podemos además ajustar un buen precio de partida estimándolo[^precioestimado]
como 
$P_E = {V_{total} \over S_{total} + K'/2}$
donde $K'$ sería la cantidad de candidaturas
con opciones a escaño, es decir ,
aquellas cuyos votos superan $P_L$.


[^precioestimado]:
La estimación supone que
las candidaturas con opción tendrán, en media,
la mitad de un escaño como restos.
Quizás la media sería un poco más alta al incluir las que casi entran,
pero estaría compensado al ignorar los restos de las muchas candidaturas
que suelen quedarse lejos de la representación.
En cualquier caso, la estimación suele funcionar bastante bien con pasadas convocatorias.
$$V_{total} = S_{total} P_E + K' P_E / 2 $$
$$P_E = {V_{total} \over S_{total} + K' / 2 }$$

Estas cotas y estimaciones del precio del escaño serán útiles, por ejemplo,
para prever el impacto real del umbral electoral (3%, 5%...)
considerando los parámetros
de la convocatoria y de la circunscripción concreta.
Para que pueda afectar el umbral éste ha de estar por encima del precio por escaño.
En la mayoría de situaciones, el umbral no tendrá efecto alguno,
pero en las pocas que lo tiene, suele ser importante.

También son útiles para determinar, por ejemplo,
la masa crítica de un voto estratégico coordinado.

## Cociente de Hare, un mundo ideal

Imaginad un "mundo ideal" en el que se pudiera descuartizar candidatos y obtener,
por ejemplo, 5'61 escaños.
Motosierra en mano, podríamos conseguir representaciones exactamente proporcionales
al número de votos.

![](/images/bloodychainsaw.jpg)

El precio a pagar por escaño en este "mundo ideal",
es el llamado _cociente de Hare_,
que coincide con la cota superior que habíamos establecido antes
para el precio de D'Hondt.

$$P_{Hare} = {V_{total} \over S_{total}}$$

Por desgracia, este tipo de descuartizamiento es ilegal en la mayoría de democracias.
Nos tendremos que quedar, como mucho, con la parte entera.
Pero, después, quedarían por repartir los escaños que quedaban fraccionados.

Si quisieramos alejarnos lo menos posible de la proporcionalidad de Hare,
la mejor opción darle un escaño extra a las opciones con mayores restos,
las que estarían más cerca de obtener el siguiente escaño.

Esto sería el [Método Hamilton](https://es.wikipedia.org/Método_Hamilton) o _de mayores restos_.
También tiene una cierta divergencia con el reparto sádico/ideal de Hare,
pero intenta ser justo en la distribución de los escaños fraccionados,
minimizando la sobre/infa-representación.

El origen de la desproporcionalidad está vinculado, pues, a los escaños fraccionados.
Contra más escaños enteros se repartan, más proporcional será el resultado.
Los escaños fraccionados están acotados entre $0$ y $K$ se pueden estimar
como la mitad de las candidaturas con opción $K'/2$.

## La proporcionalidad o no de D'Hondt

D'Hondt consiste en bajar el precio hasta que se repartan todos los escaños.
Como el coeficiente de Hare es la cota superior para dicho precio,
esto asegura que los escaños enteros de Hare se repartirán igual,
garantizando un cierto nivel de proporcionalidad.
La desproporción, otra vez, vendrá en como se repartirán los escaños fraccionados.

Partimos de los restos de Hare, como en Hamilton,
por eso podemos decir que D'Hondt también favorece a las candidaturas que se habían
quedado cerca del escaño.
Pero aquí la diferencia está que, al bajar el precio, los restos de cada candidatura
se van a nutrir con lo que al bajar el precio le sobrará a cada escaño obtenido.

Por ejemplo, si el precio se reduciera 3 votos,
una candidatura sin escaños estará 3 votos más cerca del siguiente escaño.
Pero para una candidatura con 5 escaños,
3 votos de cada uno de esos 5 escaños, ahora sobran y pasan a los restos,
por lo que estará 18 votos más cerca del siguiente escaño.

Esta ventaja de los grandes para conseguir escaño es la que
consigue la proporcionalidad hasta que llegamos a Hare.
Pero a partir de Hare, se pasa y empieza a generar desproporcionalidad.

Este beneficio es relativo.
Se nota cuando

- hay pocos escaños a repartir relativamente a las candidatura con opciones
 (y por tanto, menos escaños enteros de Hare respecto a los fraccionados)
- o cuando la desproporción entre candidaturas es notable y la ventaja es más significativa


Al final el gran disruptor de la proporción en el sistema electoral
es la división en circunscripciones, que multiplica las desproporciones
que existan en cada circunscripción.

Un método Hamilton tiene menor desproporción pero también la tiene.
Esa desproporción también se vería multiplicada por la división en circunscripciones,

Y el segundo disruptor de la proporcionalidad, 
por delante de D'Hondt, son las circunscripciones
pequeñas con pocos escaños.
Es como pintar imágenes con 4 pixeles.
Uses el método que uses no tienes precisión suficiente
para representar la realidad.

## El poder de N votos

Si existe cierta incertidumbre sobre los escaños que obtendrá una candidatura,
sus restos son aún menos predecibles.
Por eso, consideraremos que, para una candidatura X
con probabilidad de alcanzar representación,
sus restos tienen igual probabilidad de estar en cualquier punto entre 0 y $P$,
sin incluir $P$.

En ese caso, N votos tienen la misma probabilidad de ganar un escaño
para una candidatura con algunos pocos escaños que para una candidatura
con muchos escaños.
Similar probabilidad existe para ambas de perder un escaño si esos N votos se pierden.

## Un atajo para calcular D'Hondt

Como sabemos que el precio de D'Hondt será igual o menor que $P_{Hare}$,
¿por qué no empezar a calcular cocientes a partir de ese punto?

- Calculamos el cociente Hare $P_{Hare} = V_{total} / S_{total}$
- Dividimos los votos de cada candidatura por dicho precio
- Asignamos tantos escaños como la parte entera resultante
- Calculamos los coeficientes para el siguente escaño de cada candidatura
- A partir de ahí aplicamos D'Hondt: asignamos escaño al mayor coeficiente, recalculamos coeficiente y vuelta a empezar hasta que no queden escaños.

## Conclusiones

Resumiendo todo lo anterior:

- D'Hondt es un procedimiento para buscar un precio en votos por escaño,
que reparta de forma exacta los excaños disponibles, sin que sobren ni falten.

- Los cocientes que cálcula el método se corresponden con el precio máximo
con el que cada candidatura puede conseguir un número de escaños determinado.

- Escogiendo los $S_{total}$ mayores cocientes asegura que, fijando el precio
al del último cociente, se obtenga el reparto exacto.

- El mayor cociente no escogido, también sirve para acotar el precio por abajo.
El reparto exacto se da para cualquier precio entre estos dos, no incluyendo el último.

- Al final todas las candidatura tendrán un resto de votos inferior a dicho precio.
Si hay incertidumbre de los escaños que obtendrá una candidatura,
mayor incertidumbre hay en los restos, cualquier número de votos restantes es igual de posible.

- Eso determina que ganar o perder N votos ( $N < P$ )
tiene la misma probabilidad de hacer ganar o perder escaño,
tanto a una candidatura grande como a una pequeña.

- Sin hacer el reparto, podemos acotar el precio
entre el precio de una situación sin restos,
que coincide con el cociente Hare
$P_H={V_{total} \over S_{total}}$,
y el precio de una situación con restos máximos
$P_L={V_{total} \over S_{total} + K }$.

- También podemos obtener una buena estimación
del precio suponiendo que el resto medio de
las candidaturas con representación es la mitad del precio:
$P_{estimado} = { V_{total} \over S_{total} + K'/2}$.

- Tanto las cotas como la estimación son útiles, por ejemplo,
para saber cual es la masa crítica para un voto estratégico coordinado,
o para saber que efecto puede tener el umbral electoral.

- D'Hondt asegura que se repartan los escaños enteros de un reparto proporcional (Hare).
En ese sentido es bastante proporcional si hay suficientes escaños
respecto al número de candidaturas con opciones.

- Difiere de otros métodos, en como se reparten los escaños fracionados de Hare.
Si bien da relativa preferencia a quien tuviera más restos,
los reparte de forma proporcional a los escaños ya obtenidos,
lo que, a partir de los enteros de Hare, genera desproporción a favor de los grandes.

- Esta desventaja hay que relativizarla, puesto que N votos tienen el mismo poder
de otorgar escaños (o quitar si se le retiran) a una candidatura grande
que a una candidatura pequeña con representación.
Esto, explicado así, parece un poco contradictorio así que lo analizaremos con
mayor profundidad en otro artículo.

Ahora, con todas estas herramientas en la mochila,
validemos o descartemos las cosas que se dicen sobre el tema.


## Bibliografia






