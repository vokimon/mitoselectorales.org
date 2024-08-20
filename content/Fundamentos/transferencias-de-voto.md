---
title: Efecto de las transferencias de voto
date: 2024-08-20 09:03
author: David García Garzón
tags: D'Hondt, Lógica_de_Bloques, Voto_Concentrado
status: draft
cover: images/transfer-space-with-minimum.svg
---


Para desmontar algunos mitos,
es útil entender cuál es el efecto de la transferencia de votos entre formaciones.
En el anterior artículo, donde desmentíamos el mito de concentrar el voto,
hicimos algunas simplificaciones para tener una forma visual de explicarlo.
Simplificaciones y suposiciones que no demostramos del todo.
Si necesitas más pruebas, éste es el artículo que buscas.

[TOC]

## Entendiendo el Método de D'Hondt

Recapitulando lo que explica con más detalle y ayudas visuales
en el artículo [Otra manera de entender D'Hondt]({filename}entendiendo-dhondt.md),
D'Hondt busca un precio que reparta exactamente los escaños disponibles, sin que sobren ni falten.
Los coeficientes $V_X/S$ que calcula son el precio máximo por el que la candidatura X obtendría $S$ escaños.
Al seleccionar los $S_{total}$ mayores aseguramos que el precio reparta justo $S_{total}$ escaños.

:::figure /images/revote-dhondttable.png
	Cocientes de un reparto de D'Hondt real.
	Cada celda de la tabla contiene los votos obtenidos por cada partido dividido por un número de escaños.
	Los 33 mayores cocientes con el fondo azul fueron los que obtuvieron escaño,

Cuando repartimos escaños a un precio $P$,
los votos a cada formación X, se parten en tantos segmentos de tamaño $P$ como escaños obtenidos,
y un bloque de restos de tamaño menor que $P$ que no han llegado a obtener representación.

$$V_X =  S_X P + R_X$$
$$0 \le R_X < P$$

::: figure {filename}/images/dhondt-seat-rest-view.png alt="Una serie de barras con los votos a las candidaturas, divididas en segmentos de la misma longitud, que representarian los escaños, con un segmento tranlúcido al final de la barra que representarían los restos."
	La parte translúcida del final son los restos que no han llegado al siguiente escaño.

Si C es la candidatura que obtiene el último escaño
y D es a la que pertenece el mayor coeficiente que
queda fuera:

$$P_{max} = P_C = {V_C \over S_C} $$
$$P_{min} = P_D = {V_D \over S_D + 1} $$

Los precios $P$ tal que $P_{min} < P \le P_{max}$
generan un reparto exacto.


::: figure {filename}/images/trasvases-ejemplo-cociente-fijador.png
	$P_{max}$ y $P_{min}$ destacados en rojo.
	$P_{max}$, el menor de los cocientes seleccionados.
	$P_{min}$, el mayor de los cocientes no seleccionados.
	Definen el intérvalo de precios que resultan en el reparto exacto de escaños.

## Explorando el espacio de trasvases

### Escenario de partida y el espacio de escenarios post trasvase

Habiendo entendido lo que hace el método de D'Hondt,
definamos nuestro dilema.

Hay dos formaciones, A y B,
cuya suma de escaños obtenidos se pretende maximizar.
Quiero saber si hay alguna situación
en la que sea estratégicamente ventajoso para el conjunto
trasvasar un cierto número de votos entre ellas.
Por ejemplo, hay cierta percepción popular de que es mejor un trasvase a la formación mayor
y queremos saber si es cierto o si hay algún otro criterio que podamos usar estratégicamente.

Para no hacer castillos en el aire, nos anclaremos a un escenario de partida,
sobre el que aplicaremos un trasvase de votos entre A y B para evaluar su efecto.
Es incierto cuál será dicho escenario de partida,
y puede que haya unos escenarios más probables que otros.
Pero cuando apliquemos el trasvase sobre ese escenario,
hay ciertas cosas que se cumplirán:

- Los votos a los otros partidos no se alteran con dicho trasvase
- La suma de votos de A y B se mantiene, $V = V_A + V_B$.

Esto situa a los escenarios posibles después de un trasvase en una línia,
que va desde la concentracion total en A,
($V_A=V; V_B=0$),
a la concentracion total en B,
($V_A=0; V_B=V$),
incluyendo el escenario de partida en algún punto intermedio.

![Espacio de escenarios por trasvase](/images/transfer-space-domain.svg)

**Hacer un trasvase de votos entre A y B implica movernos por esta línia.**
Aunque no sepamos cual es el escenario de partida,
y, por lo tanto, el espacio o la línea en la que nos movemos,
sí que podemos parametrizar ese espacio y,
en base a esos parámetros,
entender qué posibilidades tenemos de mejorar o empeorar.

### Trasvase total como escenario canónico

En el espacio de trasvases anterior, los escenarios extremos,
es decir, los de trasvase total a una o otra opción,
nos van a servir para definir ciertos parámetros
cuyo valor determina el comportamiento de todo el espacio de trasvases.
Reducir todos los escenarios de partida posibles a estos paràmetros
nos simplificará mucho el análisis.

Dado un escenario de partida,
construyamos el escenario canónico concentrando todo el voto, por ejemplo, en A.
Como en todo escenario, se fijará un precio máximo $P_{max}$ y un precio mínimo $P_{min}$.
Como todo el voto de A y B del escenario de partida ($V$) está concentrado en A se dará que:

$$ V_A = S_A P_{max} + R_A = V $$
$$ V_B = 0 $$

Los escaños obtenidos por A ($S_A$) variarán en los otros escenarios del espacio,
por eso nos referiremos a los obtenidos en este escenario como $S$.
Igualmente, a los restos de A ($R_A$) en este escenario les llamaremos $R$.
Convertimos así a $S$ y $R$ en constantes propias, no del escenario concreto,
sino, características del todo el espacio de trasvases.

¿Qué formación está fijando $P_{max}$ en este escenario?

- B seguro que no, porque, sin votos en este escenario, todos sus cocientes son cero.
- Si lo fija A, lo fijaría su cociente $P_S = {V \over S}$. Si fuera el caso, $R = 0$.
- O podría fijarlo el menor cociente con escaño de otras formaciones, $P_C = {V_C \over S_C}$ .
En este caso, $R = {V- S P_C }$

$$ P_{max} = min(P_C, P_S) = {V-R \over S}$$

El razonamiento anàlogo lo podemos hacer para $P_{min}$ pero por abajo.

- B tampoco puede fijar $P_{min}$
- Podría fijarlo A, con su coeficiente $P_{S+1} = {V \over S+1}$
- O podría fijarlo el mayor cociente sin escaño de otra formacion D, $P_D = {V_D \over S_D +1}$ .
$$P_{min} = max(P_D, P_{S+1})$$

### Trasvasando escaños enteros

Otra herramienta útil para navegar por el espacio de trasvases
es el hecho de que si, en un escenario, se fija un precio $P_{max}$,
hacer un trasvase de $P_{max}$ votos nos lleva a un segundo escenario
en el que el el precio sigue siendo $P_{max}$ y se ha transferido
justo un escaño.

Esto se da porque si en el escenario de partida tenemos que:

$$ V_A = S_A P_{max} + R_A $$
$$ V_B = S_B P_{max} + R_B $$

En el nuevo escenario tenemos que:

$$ V_A' = V_A - P_{max} = (S_A-1) P_{max} + R_A $$
$$ V_B' = V_B + P_{max} = (S_B+1) P_{max} + R_B $$

Es decir, si en el nuevo escenario aplicara $P_{max}$,
A y B tendrían los mismos restos,
igual que pasa con el resto de formaciones que ni siquiera han variado sus votos.
Como todas las formaciones mantienen los mismos restos,
incluida la que fijaba el precio con restos cero,
$P_{max}$ será el mismo.

¿Cómo podemos usarlo? Pues por ejemplo, en un espacio donde $P_C$ marca el precio
el escenario canónico tenemos que ese precio se va a ir repitiendo a intérvalos de
trasvase $P_C$.

![Escenarios con transferencias de justo $P_C$ votos](/images/transfer-space-whole-seats.svg)

¿Quiere decir esto que el precio es una función periódica?
No exactamente, porque allà donde el precio sea menor,
el periodo también va a ser menor.
Dibujemos como evoluciona el precio y lo entenderemos mejor.

### Cuando terceros partidos no afectan

Empecemos analizando un espacio, tal que en el escenario canónico de trasvase total,
los precios $P_{max}$ y $P_{min}$ los fijan
respectivamente los coeficientes de A $P_S$ y $P_{S+1}$
y no los externos $P_C$ y $P_D$.

En el escenario de trasvase total:

$$P_{max}={V \over S} = P_S$$

Pero, según trasvasamos votos de A a B, $P_{max}$ irá bajando:

$$P_{max} = {V - V_B \over S }$$

El primer cociente de B será exactamente $V_B$.
El punto en que dicho cociente ascendente de B supere el desdendiente de A será:

$$ {V - V_B \over S}   = V_B $$
<!--
$$ V - V_B = V_B S $$
$$ V = V_B (S+1) $$
-->
$$ V_B = { V \over S + 1} = P_{S+1} $$

A partir de ese punto,
B obtendrá un escaño que arrebatará de A,
y $P_{max}$ vendrá determinado por $V_B$.

Esto seguirá así hasta que el cociente para $S-1$ escaños de A
baje lo suficiente para determinar el precio máximo.

$$ V_B = {V-V_B\over S-1} $$
<!--
$$ V_B (S-1) = V-V_B $$
$$ V_B S = V $$
-->
$$ V_B ={ V \over S} = P_S$$

Coincide con el primer precio $P_S$ a la distancia de ese mismo precio,
con lo que a partir de ahí se repite el patron:

 - Picos del precio a distancia entre ellos de $P_S={V\over S}$
- Valles cada $P_{S+1}= {V\over S +1}$ que delimitan el cambio en la distribución del escaño.


![Escenario donde A y no C fija el precio máximo para el reparto exacto](/images/transfer-space-without-pc-effect.svg)

Esto divide el espacio en $S+1$ zonas, de igual tamaño ($V\over S+1$),
con diferentes distribuciones de escaño, de 0 a $S$ escaños cada una.
Observamos también que en este escenario la suma de escaños no cambia nunca,
con lo que un traspaso, podría cambiar la distribución interna de los escaños,
pero no afectaría a la suma.

### Efecto de $P_C$, transfiriendo restos

¿Qué pasa si en el escenario canónico de trasvase total,
$P_{max}$ lo define una tercera formacion C con cociente $P_C= {V_C \over S_C}$?

$P_C$ seguirá marcando el precio máximo hasta que A haya trasferido $R$ votos a B.
En ese punto, A marcará el precio hasta que, de igual manera que antes,
el primer cociente de B supere $P_{S+1}$.
La zona de dominio de B, también se acorta de $P_S$ a $P_C$,
pero lo importante es que el punto de cambio del reparto de escaños es el mismo:
cada $P_{S+1}$ votos.

![Escenarios de precio variable con S=5](/images/transfer-space-not-considering-d.svg)

### Cuando D les quita un escaño

¿Qué pasa cuando en el escenario canónico es D quien define $P_{min}$?
Eso quiere decir que $P_D > P_{S+1}$,
así que cuando A marca el precio y va perdiendo votos,
no va a llegar a $P_{S+1}$.
Va a haber un momento en que el cociente $P_D$ se quede con el último escaño,
arrebatàndoselo al tandem A-B.
Cuando el cociente entrante de B supere $P_D$, el escaño se volvera a recuperar.

![TODO: Secamos las líneas obliquas con la constante $P_D$](/images/transfer-space-with-minimum.svg)

Esta situación es la más interesante desde el punto de vista estratégico,
porque si el escenario de partida está en una zona donde D se lleva el último escaño,
un trasvase podría devolverlo.
Pero también, si no está en una de esas zonas, se podría acabar en una de ellas tras un trasvase y perder un escaño.

Las zonas verdes, en las que se mantienen los escaños del escenario canónico ($S$),
son de anchas igual que los restos de dividir los votos conjuntos a precio $P_D$ entre $S$.

$$ Vup = V - P_D S $$
$$ Vup = S(P_S - P_D ) $$

Las zonas rojas, en las que se pierde un escaño tienen de ancho:

$$ Vdown = P_D - Vup = P_D - V + P_D S $$
$$ Vdown = P_D (S+1) - V $$
$$ Vdown = (S+1) (P_D - P_{S+1}) $$

El espacio de trasvases lo compondrían
$S+1$ bandas de $V - P_D S$ de ancho en las que se obtendrian $S$ escaños,
intercaladas por $S$ bandas de $P_D (S +1) - V$ en las que se obtendria $S-1$ escaños.

Sin perdida de generalidad podemos considerar los casos anteriores
como un caso particular de este último caso, cuando $P_D = P_{S+1}$
y por tanto $ Vdown = 0 $, es decir nunca se baja a $S-1$ escaños conjuntos
siempre serían $S$.

## Resumen del espacio

Recordemos que desconocemos el escenario de partida,
y por lo tanto no sabemos en qué línea estamos moviendonos,
ni de qué punto de la línea partimos.
Lo que sabemos es que ciertos parámetros en ese espacio se van a mantener.

De lo que hemos visto dentro de esa línea,
la variación del resultado conjunto tras un trasvase solo podría ser de un escaño arriba o abajo.
Sería un escaño arriba si partimos de un escenario $S-1$ y el trasvase nos lleva a uno $S$.
Sería un escaño abajo si partimos de un escenario $S$ y el trasvase  nos lleva a uno $S-1$.
Para cualquier otro caso, no habría cambio.




Para tener una ganancia se tienen que cumplir dos condiciones:

- Que 


Para que un trasvase consiga unavance,
deberíamos estar en una zona de $S-1$ que hemos visto
Si estamos en un punto en que la suma es $S-1$


- Que estemos en una situación en que no hay 


Vemos que solo hay tres posibilidades segun donde 

- +1 Que la situacion de partida esté una zona de bajada y el trasvase sirva para llegar a una de subida
- -1 Estar en una zona de subida y saltar a una de bajada
- 0 Estar en una zona de subida o de bajada y quedarse igual


## Probabilidades

Con el espacio caracterizado, pasamos a considerar probabilidades.

Hay una cosa a destacar del espacio de trasvases cuando hay zonas en las que el resultado conjunto baja.
Las zonas de subida y bajada se alternan,
pero las zonas de bajada son $S$, mientras que las zonas de subida son $S+1$.
Si no tenemos ninguna certeza de en qué zona estaremos la probabilidad de estar en zona de bajada
es

$$ (P_D (S+1) - V) S \over V $$





Una vez hemos caracterizado el espacio de trasvases,
nos empezamos a mover en el espacio de las probabilidades.
Debemos combinar diversas incertidumbres.

La primera es la incertidumbre propia de saber cual es la situación de partida.
La seguna incertidumbre es la del número de votos que podemos conseguir trasvasar.



La situación de partida se estima a partir de sondeos y estadísticas.

La probabilidad de que se esté en un determinado tipo de escenario,
y dado ese escenario la probabilidad de que 


Cuán probable es que estemos en un cierto escenario de partida,
o mejor dicho un escenario de partida con ciertas características,
y, para cada escenario, cuán probable es que un travase de
N votos consiga un movimiento en el número de escaños totales.





## Bibliografia


https://web.archive.org/web/20180728202050/http://kenbenoit.net/pdfs/PA84-381-388.pdf



