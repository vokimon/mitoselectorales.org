title: Entendiendo la regla de D'Hondt
autor: vokimon
date: 2019-01-11
status: published
tags: D'Hondt, Coaliciones
cover: images/revote-maxminprice.gif
covercaption: El precio de D'Hondt

<!-- PELICAN_BEGIN_SUMMARY -->

En este artículo se explica, de una forma diferente y gráfica,
la Regla de D'Hondt, el sistema responsable del reparto de
representantes en nuestro sistema electoral.

Si en vez de centrarnos en el proceso de cálculo,
nos centramos en su propósito,
entendremos de forma más clara lo que está pasando.
D'Hondt pretende
**encontrar un precio en votos por el que repartir los escaños
sin que sobre ni falte ninguno**.

Con ese enfoque se observa claramente
donde está su famoso favor a los mayoritarios,
los casos en los que se da y sus límites.
También permite conocer la **masa crítica para que pasen ciertos cambios**,
y establecer la base para descartar **mitos y ideas preconcebidas**.
Mitos como
que D'Hondt es la principal responsable de la desproporción
cuando lo son las [circumscripciones]({tag}circumscripciones),
o que las [coaliciones
se ven mágicamente beneficiadas]({filename}/Parlament2015/2014-12-05-CoalicionsUnitariesConfluencies.md)
por D'Hondt.

<!-- PELICAN_END_SUMMARY -->

## TL;DR (Demasiado Largo; No Leí)

Todos tenemos muchas cosas que hacer
y este artículo, aunque tiene gráficos y animaciones, y aporta
una perspectiva clarificadora de D'Hondt, es largo.
Así que para tu conveniencia, resumo aquí las conclusiones:

- Si bien D'Hondt beneficia a los mayoritarios,
otros elementos de la ley electoral como la división
en circumscripciones tienen un impacto mucho mayor en ese sentido.
- D'Hondt respeta el reparto de **escaños enteros** que haría un reparto puramente proporcional
- La distorsión, pues, la provoca el reparto de los escaños que no se repartirían enteros, los **escaños partidos**
	- Son siempre menos que el número de candidaturas
	- Tienden a ser poco menos que la mitad del número de candidaturas con opción a representación
	- Se reparten mas o menos proporcionalmente a los escaños enteros
		- Por ejemplo: para recibir 3 extras, hay de tener aproximadamente 3 veces los escaños enteros de quien recibe 1 extra
- Por eso solo hay grandes beneficios por D'Hondt cuando hay grandes desigualdades
- Y como hay pocos extras a repartir, los beneficios suelen limitarse a 2, en las grandes circumscripciones, y, históricamente como mucho a 4
- Aunque parezca paradógico,
D'Hondt no da ninguna ventaja a las coaliciones
que no les de ya por separado.
El beneficio es la suma de restos de votos,
que se da en cualquier otro método
y esta limitada a 0 o 1 escaños por circumscripción.
- D'Hondt acaba fijando un precio para el escaño:
	- Saber ese precio, nos da una idea de la **masa crítica para tener impacto**
	- Dada la participación, se puede acotar por arriba y por abajo
	- Dada la participación tiene un valor esperado

En este mundo, no hay tiempo para contrastar, leer o reflexionar.
Pero recuerda:
Los mitos se propagan porque la gente en general se cree
lo que lee en Internet si está en un formato guai y más o menos le cuadra.
Te puedes quedar con estas conclusiones
o puedes seguir leyendo y entender porqué
y como de grises son los grises.

## Se le llama _ley_, pero no es una ley legal

A menudo, se oye llamar _Ley de D'Hondt_ a la ley electoral.

Por eso, aclarémoslo de entrada:
la _Ley de D'Hondt_ es una ley matemática, como la _regla de tres_,
no una ley legal.
La ley electoral, la legal, es la [LOREG] que incluye,
entre muchas otras cosas,
la Regla de D'Hondt como método de reparto de escaños.
Para no ahondar en la confusión,
prefiero usar la palabra _regla_ (o _método_, o _sistema_).

## Unos tienen la fama y otros cardan la lana

Se dice también que la Regla de D'Hondt es la responsable de que
la ley electoral beneficie a las opciones mayoritarias.

Y sí, realmente la Regla de D'Hondt beneficia a los mayoritarios.
Pero es que la LOREG en general contiene muchos otros elementos
que benefician a los mayoritarios con el pretexto de la **gobernabilidad**.
La Ley de D'Hondt es sólo uno de ellos,
y de hecho no es el que tiene más impacto.
Las que cardan la lana son las circumscripciones.

La división en circumscripciones distorsiona por dos motivos principales:

- Por un lado genera un efecto umbral muy acusado (20%-40%)
en las numerosas circumscripciones pequeñas con 3 o 4 diputados.

- Por otro multiplican la distorsión que provoque D'Hondt
o cualquier regla que usemos para repartir.
Como es ilegal en España entrar con la motosierra a los parlamentarios,
uses el reparto que uses, siempre habrá alguna distorsión.
**Tiene menos impacto tener 10 escaños mal repartidos
en una circumscripción única,
que tener un solo escaño mal repartido
en cada una de las 52 circumscripciones actuales.**

Por eso, a los actuales y futuros renovadores de la ley electoral:
Sí. D'Hondt es mala y molaría substituirla.
Pero invertid los esfuerzos en reformar primero las circumscripciones.
**Eso sí ¡no para hacerlas [aún más pequeñas][Veguerias], por favor!**

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

## Acorralando el precio de D'Hondt

Puesto que el reparto de D'Hondt se base en ajustar el precio del escaño,
muchas cosas dependen de él y nos interesa acotarlo.
Por ejemplo para conocer cuál es la **masa crítica para cambiar las cosas**,
o para saber si el **umbral electoral**,
que suele ser del 3% según la convocatoria,
tiene efecto o es totalmente inútil.

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
todas las formaciones menos una se quedarían a un voto del siguiente escaño.

Estos dos ejemplos de escenarios extremos están disponibles en el simulador.
La zona translúcida son los votos que no han servido para sumar escaño.

[
![Igual votos a candidaturas, igual resultado, máximo y mínimo precio]({static}/images/revote-maxminprice.gif)
Dos escenarios con el mismo número de votos a candidaturas, y el mismo resultado, 
uno con el precio máximo y otro con el precio mínimo
]({static}/images/revote-maxminprice.gif){style=text-align:center}

El precio final es exactamente:

$$ Precio_{real}
= { Votos \over Escaños + Candidaturas · R }
$$

Donde `R` es la media de las porciones de escaño sin completar
a las candidaturas.

Por ejemplo si en media, las candidaturas 
se han quedado a medio camino entre un escaño y el siguiente:

$$ R = {1\over 2} $$

De hecho eso es lo que tiende a pasar con todas las candidaturas con opciones
a tener representacion.
Con la misma probabilidad pueden quedarse
en cualquier punto entre el mismo escaño y el siguiente.
Por eso el resto esperado es medio escaño.

Sin embaro, eso no suele pasar con las candidaturas extraparlamentarias.
Suelen quedarse siempre por debajo del 30%.
Así que normalmente `R` sera un factor por debajo de 0,5.

Si para una convocatoria y circumscripción concreta
sabemos mas o menos el número de candidaturas que se quedarán
fuera, y más o menos los votos medios,
podemos ajustar más R.

Hace rato que entrado hace rato en el mundo de la aproximación.
En el simulador de flujos electorales aparecen estos factores
cuando abres un escenario electoral concreto,
así que puedes ver los valores típicos para la convocatoria
que te interese.

## Acotando la desproporción

Hemos comentado que cuando tenemos precio máximo,
nos sale una proporción exacta con los votos.
Si aplicáramos ese precio a un escenario cualquiera,
normalmente no salen escaños enteros.
Tendríamos que andar con la motosierra y los diputados y eso no es legal en España.
Al final tendríamos escaños que estan partidos entre varias opciones
que no se reparten, y opciones con votos de sobra.

La forma más natural (¡y justa!) de repartir esas sobras
es la que se llama
[Regla de Hamilton](https://es.wikipedia.org/wiki/Regla_de_Hamilton)
o de _restos mayores_.
Lo que hace es
repartir los escaños sobrantes a las opciones con más restos de votos,
que por tanto se habían quedado más cerca de obtener el siguiente escaño.
Esto minimiza los votos que estan representados
por una opción que no es la que escogieron, aunque siguen habiéndolos.
Cada opción como máximo se lleva un escaño extra o ninguno.

Pero D'Hondt reparte los restos de una forma distinta.
Va reduciendo el precio hasta que se acaban repartiendo todos.
Si con el precio máximo una opción ya ha obtenido N escaños,
bajando el precio solo puede obtener más.
Así que de entrada concluimos que **tanto Hamilton como D'Hondt
reparten como mínimo los escaños que quedan enteros en un reparto puramente proporcional.**

La posible desproporción es la que cause el reparto de los escaños sobrantes.

¿Sabemos cuantos escaños sobrarán?

Como poco, ninguno, en el caso ideal de escaños justos.
Como mucho, a todas las candidaturas les sobraría casi un escaño,
menos a una candidatura que tendría lo que les falte a las otras.
Serían el número de candidaturas menos una.

En un escenario típico, vuelven a ser la mitad de las candidaturas
con opción mas los restos de las extraparlamentarias.
Atención, por eso porque ahora estamos hablando de los restos
en el reparto puramente proporcional, y antes de los restos de D'Hondt.


## Una desproporción proporcional

Ya hemos aproximado lo que vale un escaño.
Hemos visto que la desproporción solo puede venir de los escaños de restos,
y sabemos aproximadamente cuantos escaños son.

Veamos cómo reparte los restos la regla de D'Hondt:

Si se baja el precio,
una opción con más votos sobrantes
tiene más probabilidades de llegar al siguiente.
Esto sería igual que Hamilton:
Un escaño arriba o no, y se lo llevan las opciones con más restos.

La diferencia radica en un pequeño detalle:
Si, para repartir todos los escaños, hay que bajar el precio,
digamos a un 90%,
no solo estamos rebajando el umbral al que tienen que llegar los restos.
También liberamos un 10% de votos que usabamos para cada escaño entero que obtuvimos con el precio máximo
y que ahora pasarán a formar parte de los restos.

Tanto es así que, por ejemplo, una formación con 9 escaños, y un 10% de rebaja en el precio,
llegaría sí o sí al 90% del siguiente escaño, tenga los restos que tenga.
Es más, una formación con 18 escaños llegaría al segundo extra tenga los restos que tenga.
Y entre medias una ventajita, proporcional a los escaños enteros.

Como ves, esta ventaja es proporcional a los escaños enteros
que al mismo tiempo es más o menos proporcional a los votos.
Pero no deja de ser una desproporción, porque la proporción
ya la teníamos más o menos con los escaños enteros
y al añadir más de un escaño con seguridad la estamos rompiendo.

Pero el hecho de que se aproximadamente proporcional tiene un efecto paradójico con las coaliciones.
Imaginemos dos formaciones que habrían obtenido 8 y 3 escaños enteros en la repartición proporcional.
Por separado D'Hondt les da 8 y 3 veces los votos que se ha tenido que reducir el precio.
Juntos obtendrían 11 escaños enteros o, con una probabilidad del 50%, quizas 12 por la suma de los restos.
11 es la suma de la ventaja que ya tenían por separado.
Podría ser 12 pero si ya han sumado los restos, los nuevos restos son menos del 50%,
así que generalmente el único beneficio de la coalición es la suma de restos
que ya sucede con una distribución de Hamilton.


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
[Veguerias]:{filename}/Parlament2015/2015-02-03-VegueriesYElTimoDeLaEstampita.md


