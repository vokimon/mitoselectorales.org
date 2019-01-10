title: Entendiendo la regla D'Hondt
autor: vokimon
date: 2018-12-12
status: published
tags: D'Hondt, Coaliciones

### Unos tienen la fama y otros cardan la lana

Podríamos hilar una serie de medias verdades verosímiles
que circulan sobre D'Hondt y acabar en conclusiones muy peligrosas
para la salud (democrática del país).
Por ejemplo:

> **Creencia popular:**
> El sistema electoral se rige por la Ley D'Hondt,
> Es una ley injusta que beneficia a las candidaturas mayoritarias.
> Mientras que siga vigente esa ley,
> es mejor hacer coaliciones de partidos para que no nos penalice.

<!-- PELICAN_END_SUMMARY -->

Puntualicemos:

- D'Hondt es una ley matemática (o regla, como la "regla de tres"), no una ley civil/legal. La ley legal es la LOREG.
- La LOREG favorece mucho a los mayoritarios,
y el uso de la regla D'Hondt tiene parte de culpa,
pero no es el único aspecto de la ley que lo hace,
ni siquiera el que más.
La mayor desproporción esta causada por la división en [circumscripciones electorales]({tag}circumscripciones).
- D'Hondt es _proporcionalmente desproporcionada_, los escaños de más que se llevan son proporcionales al tamaño.
Si sumas los resultados de dos candidaturas, sumarán los escaños de más que ya tenian por separado.
- Si que hay un efecto beneficioso de juntarse, pero no es por D'Hondt es por la suma de restos
y su efecto esta limitado a un escaño o no en cada circumscripcion.

Así que, no, D'Hondt no beneficia especialmente las coaliciones respecto a ir separado.
Hay ventaja, pero una más pequeña, la de la suma de restos, que tendríamos tambien si usaramos otra regla.

Te lo puedes creer como nos creemos todos estos mitos, porque lo dice Internet,
o podemos entender un poco mejor como funciona la regla D'Hondt.

## Entendamos el objetivo, no el procedimiento

En la LOREG, y en la mayoría de fuentes,
se explica D'Hondt describiendo el procedimiento para calcularlo:

> Para cada candidatura, obtienes sus cocientes dividiendo los votos recibidos por 1, 2, 3, 4...
> asignas escaño a los cocientes más altos,
> bla, bla, bla...

![Cocientes del Método D'Hondt
para las Generales del 1079 en Barcelona
]({static}/images/revote-dhondttable.png)


Esta descripción es útil para que burócratas e informáticos calculen el reparto sin pensar.
¿Pero para qué se hace todo eso?
Es mucho más ilustrador si explicamos D'Hondt por su objetivo:

> D'Hondt sirve para encontrar un precio en _votos por cada escaño_,
> tal que, a ese precio
>
> - se reparten todos los escaños disponibles
> - a ninguna candidatura le sobran votos para ningun escaño más

En vez de usar el método D'Hondt de los cocientes,
podríamos llegar al mismo resultado moviendo el precio
hasta encontrar uno que reparta el número justo de escaños.

![Animación: Ajustando el precio hasta que se reparten todos los escaños
]({static}/images/revote-dhondtbars.png)

Todo el tema de precios que se fijan solos
suena mucho a la [mano invisible del mercado][AdamSmith].
Quizás por eso les sonó tan _bueno y justo_ a las democracias liberales del siglo pasado.

En todo caso, parece proporcional, ¿verdad?
Pues lo es bastante aunque no del todo.
Si le damos un par de vueltas,
entenderemos un poco mejor donde está la desproporción,
en qué casos se da y qué papel juega.

## Delimitando la búsqueda

Esa búsqueda del _precio justo_,
se puede delimitar entre dos casos extremos.

El precio màximo posible se da en el improbable caso en que no le sobrara a nadie votos.
Todas las candidaturas tienen los votos justos para sus escaños.

$$ Precio_{máximo} = { votos \over escaños } $$

El precio mínimo sería en otro caso muy improbable en que a todas las candidaturas
(menos una)
se quedasen a un solo voto del precio para conseguir el siguiente escaño.
La fórmula (simplicada) sería:

$$ Precio_{minimo} = { votos + candidaturas - 1 \over escaños + candidaturas - 1 }
\approx { votos \over escaños + candidaturas }
$$


## Un mundo ideaaaaal

De los dos casos extremos, el que obtiene un representación
más ajustada a la realidad de la población es el primero,
aquel que no sobran votos, todos los votos tienen representación
y la proporción de votos correspondería con la proporción de escaños.

Por ejemplo si tenemos:

$$ VotoACandidaturas = 2.000.000;  Escaños = 20 $$
$$ PrecioPorEscaño = 100.000 votos/escaño$$

Y todas las candidaturas consiguieran un multiplo de 100.000 votos:
700mil, 600mil, 400mil, 200mil y 100mil,
repartiríamos 7, 6, 4, 2 y 1 escaños.
Las proporciones en el parlamento serían las mismas que en la sociedad,
ignorando el no-voto.

Pero en un caso real, tendríamos escaños que estan repartidos
entre varias opciones.
Por ejemplo si una opción tiene 230mil le tocarían 2'3 escaños.
La realidad es que no estamos en un mundo ideal
y es ilegal usar la motosierra para mutilar diputados.
Así que tenemos que encontrar una forma de repartir esos escaños partidos.

La forma más natural (¡y justa!) de repartir esas sobras
es la que se llama
[Regla de Hamilton](https://es.wikipedia.org/wiki/Regla_de_Hamilton)
o de _restos mayores_.
Lo que hace es repartir los escaños sobrantes a las candidaturas
que se han quedado más cerca de obtener el siguiente.
Si a una formación le sobran 20mil votos y a otra 80mil,
se lo queda la de 80mil.
Como mucho a cada formación le daríamos un escaño adicional,
así que no nos desviaríamos mucho del ideal.

Pero D'Hondt no hace eso.
D'Hondt va bajando el precio hasta que se reparten todos los escaños
y eso es un chollo para las candidaturas con más votos.


## La subasta

Hacemos una subasta a la baja.
Partamos del precio máximo,
el que sería ideal si tuvieramos la motosierra,
y vamos bajando hasta que se repartan enteros
todos los escaños disponibles.

Digamos que para un reparto en concreto
D'Hondt tiene que bajar el precio a un 90% del precio original.
En el ejemplo de arriba equivale a bajar de 100mil a 90mil votos.
Una formación que solo tuviera 90mil ya conseguiría su primer escaño.
De echo todos los que estaban a 90mil votos del siguiente escaño
lo consiguen.
Más o menos como Hamilton, pero hay un segundo efecto.

A cada escaño entero que cada candidatura había conseguido en el reparto de la motosierra,
ahora le sobra un 10% que se suma a los restos.
Contra más escaños tengas en el reparto de la motosierra,
más 10% se te suman a los restos.
De hecho, si tienes 9 escaños, 9 x 10mil = 90mil,
tienes un escaño extra asegurado.
Si tienes 18 escaños, dos escaños extras asegurados.

Así que ya no solo es el hecho como pasaba en Hamilton
de estar más cerca o lejos del siguiente escaño,
sinó que se suma una ventaja que es proporcional
a los escaños enteros que tengas en el reparto inicial.

## ¿Cuántos escaños sobrantes se reparten?

Si al reparto entero le sobran 2 o 3 escaños,
igual no hay mucho espacio para la desproporción,
si sobran 10, puede ser bastante abultado.
¿De qué depende?

Están delimitados por los mismos casos extremos que el precio.


Cuál es el alcance de esta desproporción?

El número de escaños repartibles a los restos depende
de los escaños que no se puedan repartir.
Lo máximo sería un escaño por candidatura menos una.









## Gobernabilidad vs Proporcionalidad



Pero no, a los políticos no les mola Hamilton, porque prefieren
lo que llaman **gobernabilidad** a la **proporcionalidad**.
Por lo visto, un país es ingobernable si no manda una persona o grupo con poder para hacer y deshacer a su antojo.
Por lo visto, los poíticos necesitan no tener que pactar con nadie para gobernar bien.
No sabemos gobernarnos entre todos si no hay un lider que nos diga el camino.
TODO: Calcular la experanza dado un tanto por ciento de cambio en el precio segun los escaños que tengas.

Eso quiere decir que una candicatura con:

- 0 escaños, recibe uno más si sus restos llegan a 90mil
- 1 escaño, a 80mil
- 3 escaños, a 60mil
- 9 escaños, toma uno seguro, y si los restos eran 90mil tambien el siguiente

El problema aquí es que estamos repartiendo los restos de forma proporcional,
pero rompiendo la proporcionalidad que ya teníamos.

P'=f·P
ri' = ri + Ei*(1-f)*P
^Ei = ri' // P'
^Ei = (ri + E·P(1-f)) // P'
^Ei = (ri + E·P(1-f)) // (f·P)
^Ei = (ri + E·P - E·P·f)) // (f·P)
^Ei = ri/ (Pf) + E(1-f/f)

P < V / E
P > V / (E + C)


cand |   votos|   escaños|
-----|--------|----------|
A |  2.000 | 1
B |  4.000 | 2
C | 16.000 | 8
D | 18.000 | 9
Suma | 40.000 | 20

Pero es muy improbable. Tendríamos más algo como esto:

cand |   votos|   escaños|
-----|--------|----------|
A |  2.100 | 1'05
B |  3.700 | 1'45
C | 16.000 | 8
D | 18.000 | 9


(E + Cf) P = V

V = E*P + (C-1) (P-1)

V +c -1 = P (E+C-1)

P = (V+C-1) / (E+C-1)






[LOREG]: http://www.juntaelectoralcentral.es/cs/jec/loreg
[LeyesAutonomicas]: https://espana.leyderecho.org/normativa-electoral-autonomica/
[AdamSmith]: https://es.wikipedia.org/wiki/La_riqueza_de_las_naciones

