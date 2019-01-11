title: Entendiendo la regla D'Hondt
autor: vokimon
date: 2019-01-11
status: published
tags: D'Hondt, Coaliciones
cover: images/revote-maxminprice.gif
covercaption: El precio de D'Hondt

## Unos tienen la fama y otros cardan la lana

<!-- PELICAN_BEGIN_SUMMARY -->

Podríamos hilar una serie de medias verdades verosímiles
que circulan sobre D'Hondt y acabar en conclusiones muy peligrosas
para la salud (democrática del país).
Por ejemplo:

> **Creencia popular:**
> El sistema electoral se rige por la Ley D'Hondt.
> Es una ley injusta que beneficia a las candidaturas mayoritarias.
> Cuando derroguemos D'Hondt todo será más proporcional.
> Mientras que siga vigente esa ley,
> es mejor hacer coaliciones de partidos para que no nos penalice.

<!-- PELICAN_END_SUMMARY -->

¿Qué cosas no son ciertas?

- Primero, D'Hondt es una ley matemática (o regla, como la "regla de tres"),
no una ley civil/legal como mucha gente piensa.
La ley legal es la [LOREG].
- La LOREG tiene muchos elementos que favorecen a los mayoritarios.
El uso de la regla D'Hondt es uno de ellos,
pero apenas tiene efecto en comparación con lo que afectan las [circumscripciones]({tag}circumscripciones).
- D'Hondt es _proporcionalmente desproporcionada_, los escaños de más de cada candidatura son proporcionales al tamaño.
Si sumas los resultados de dos candidaturas, sumarán los escaños de más que ya tenian por separado.
- Si que hay un efecto beneficioso de juntarse, pero no es por D'Hondt es por la suma de restos
y su efecto esta limitado a un escaño o no en cada circumscripcion.

Así que, no, D'Hondt no beneficia especialmente las coaliciones respecto a ir separado.
Hay ventaja, pero una más pequeña, la de la suma de restos, que tendríamos también si usáramos otra regla,
y es una ventaja tan pequeña que puede no ser suficiente si los electores no están de acuerdo con la coalición.

Y, ahora, te puedes creer lo que digo como nos creemos todos estos mitos,
porque lo dice Internet,
o podemos entender un poco mejor como funciona la regla D'Hondt
para comprobar si lo que digo es cierto o no.

## Entendamos el objetivo, no el procedimiento

En la LOREG, y en la mayoría de fuentes,
se explica D'Hondt describiendo un aburrido procedimiento para calcularlo:

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
> - se repartan todos los escaños disponibles
> - a ninguna candidatura le sobren votos para ningun escaño más

En vez de usar el método D'Hondt de los cocientes,
podríamos llegar al mismo resultado moviendo el precio
hasta encontrar uno que reparta el número justo de escaños.

![Animación: Ajustando el precio hasta que se reparten todos los escaños
]({static}/images/revote-fittingprice.png)

Todo lo que suene a precios que se fijan solos
recuerda mucho a la [mano invisible del mercado][AdamSmith].
Quizás por eso les sonó tan _bueno y justo_ a las democracias liberales del siglo pasado.

En todo caso, parece proporcional, ¿verdad?
Pues lo es bastante, aunque no del todo.
Si le damos un par de vueltas,
entenderemos un poco mejor donde está la desproporción,
en qué casos se da y qué papel juega.

## Delimitando la búsqueda

Es muy útil entender que esa búsqueda del _precio justo_,
está delimitada entre dos casos extremos.

El **precio màximo** posible se da en el improbable caso en que no le sobrara a nadie votos.
Todas las candidaturas tienen los votos justos para sus escaños.

$$ Precio_{máximo} = { Votos \over Escaños } $$

Por ejemplo, si tenemos 2.000.000 de votos a candidaturas y 20 escaños a repartir,
el precio máximo será 100.000 votos por escaño.

Para que se de ese precio,
todas las candidaturas tendrían que tener un múltiplo de 100.000 votos.
Por ejemplo: 700mil, 600mil, 400mil, 200mil y 100mil.
Y les repartiríamos 7, 6, 4, 2 y 1 escaños respectivamente.

Como ves, sería el caso ideal porque
las proporciones en el parlamento serían las mismas que en la sociedad,
ignorando el no-voto.

El **precio mínimo** sería el caso opuesto, también muy improbable,
en que a todas las candidaturas (menos una)
se quedasen a un solo voto del precio para conseguir el siguiente escaño.
Dado el número de votos a candidaturas, los escaños y el número de candidaturas,
podemos conocer ese precio mínimo.

$$ Precio_{minimo}
= { Votos + Candidaturas - 1 \over Escaños + Candidaturas - 1 }
%\approx { Votos \over Escaños + Candidaturas }
$$

Para el caso anterior, el precio mínimo seria 83.333,5.
Por ejemplo, si los votos fueran: 583.334, 583.333, 416.667, 250.000 y 166.666,
todas las formaciones obtendrían el mismo resultado y 
todas menos la primera se quedarían a un voto del siguiente escaño.

Estos dos ejemplos de escenarios extremos están disponibles en el simulador.
La zona translúcida son los votos que no han servido para sumar escaño.

[
![Igual votos a candidaturas, igual resultado, máximo y mínimo precio]({static}/images/revote-maxminprice.gif)
Dos escenarios con el mismo número de votos a candidaturas, y el mismo resultado, 
uno con el precio máximo y otro con el precio mínimo
]({static}/images/revote-maxminprice.gif){style=text-align:center}

## Acotando la desproporción

Hemos comentado que cuando tenemos precio máximo,
nos sale una proporción exacta con los votos.
Si aplicáramos ese precio a un escenario cualquiera,
normalmente no salen escaños enteros.
Tendríamos que andar con la motosierra y los diputados y eso no es legal en España.
Al final tendríamos escaños que estan partidos entre varias opciones
y no se reparten, y opciones con votos de sobra.

La forma más natural (¡y justa!) de repartir esas sobras
es la que se llama
[Regla de Hamilton](https://es.wikipedia.org/wiki/Regla_de_Hamilton)
o de _restos mayores_.
Lo que hace es
repartir los escaños sobrantes a las opciones con más restos de votos,
que se habían quedado más cerca de obtener el siguiente.
Cada opción como máximo se lleva un escaño extra o ninguno.

Pero como hemos dicho, D'Hondt lo que hace es ir bajando el precio hasta que se reparten todos.
Si bajamos el precio y con el precio máximo una opción ya ha obtenido N escaños,
bajando el precio solo puede obtener más.

Así que de entrada concluimos que

- D'Hondt reparte como mínimo los escaños enteros al precio máximo, igual que Hamilton
- La desproporción de D'Hondt es la que cause el reparto de esos escaños sobrantes

¿Sabemos cuantos escaños sobrarán?

Como poco, ninguno, en el caso ideal de escaños justos.
Como mucho, a todas las candidaturas les sobraría casi un escaño,
menos a una candidatura que tendría lo que les falte a las otras.
Serían el número de candidaturas menos una.


## Una desproporción proporcional

Veamos cómo reparte los restos la regla de D'Hondt:

Si se baja el precio,
una opción con más votos sobrantes
tiene más probabilidades de llegar al siguiente.
Esto sería igual que Hamilton:
Un escaño arriba o no, y se lo llevan las opciones con más restos.

La diferencia radica en un pequeño detalle:
Si, para repartir todos los escaños, hay que bajar el precio, digamos a un 90%,
no solo estamos rebajando el umbral al que tienen que llegar los restos.
También liberamos un 10% de votos que usabamos para cada escaño que obtuvimos con el precio máximo
que ahora pasarán a formar parte de los restos.

Tanto es así que, por ejemplo, una formación con 9 escaños, y un 10% de rebaja en el precio,
llegaría sí o sí al 90% del siguiente escaño, tenga los restos que tenga.
Es más, una formación con 18 escaños llegaría al segundo extra tenga los restos que tenga.
Y entre medias una ventajita, proporcional a los escaños enteros.

Como ves, esta ventaja es proporcional a los escaños enteros
que al mismo tiempo es más o menos proporcional a los votos.

## Conclusiones

- D'Hondt reparte los escaños enteros igual que lo hace Hamilton
- La diferencia está en cómo se reparten los escaños sobrantes
- Los escaños sobrantes pueden ser de 0 a al número de candidaturas (menos uno)
- Los escaños sobrantes suelen ser la mitad de las candidaturas con opciones a escaño
- Si hay muchas opciones extraparlamentarias, pueden añadir un escaño sobrante extra
- D'Hondt reparte escaños sobrantes de forma proporcional, generando desproporcionalidad
- Al repartirse de forma proporcional, no beneficia a las coaliciones más allá de la suma de restos que dan medio escaño por candidatura añadida



## Apéndice: Cálculos

### Precio máximo {id=preciomáximo}

Todos los escaños se reparten a precio máximo, sin sobras.

$$ Votos = Escaños · Precio $$

$$ Precio = {Votos \over Escaños} $$

### Precio mínimo {id=preciomínimo}

A todas las candidaturas menos a una les falta un voto para llegar al siguiente.

$$ Votos = Escaños · Precio + (Candidaturas-1) · (Precio-1) $$

$$ Votos = Escaños · Precio + Candidaturas · Precio - Candidaturas - Precio +1 $$

$$ Votos + Candidaturas - 1 = Precio · ( Escaños + Candidaturas - 1 ) $$

$$ Precio = { Votos + Candidaturas - 1 \over Escaños + Candidaturas - 1 } $$

Cuando los votos son miles o millones se puede aproximar más fácil por:

$$ Precio = { Votos \over Escaños + Candidaturas - 1 } $$



[LOREG]: http://www.juntaelectoralcentral.es/cs/jec/loreg
[LeyesAutonomicas]: https://espana.leyderecho.org/normativa-electoral-autonomica/
[AdamSmith]: https://es.wikipedia.org/wiki/La_riqueza_de_las_naciones

