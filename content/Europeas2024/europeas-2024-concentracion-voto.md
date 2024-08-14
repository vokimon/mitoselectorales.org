---
title: Europeas 2024: ¿Hay que concentrar el voto?
date: 2024-06-03 09:03
author: David García Garzón
tags: D'Hondt, Europeas, Lógica_de_Bloques, Voto_Concentrado
status: published
cover: images/hay-que-concentrar-el-voto.png
---

<!-- PELICAN_BEGIN_SUMMARY -->

Europeas 2024.
Muchos partidos insisten con un mensaje:
«Para que le vaya bien a nuestro bloque ideológico,
hay que concentrar el voto en nuestro partido que es el grande».
No son tontos... ni sinceros.

Te explicamos visualmente que NO funciona así.
Todos los bulos se apoyan en cierta verdad
que después transgiversan.

<!-- PELICAN_END_SUMMARY -->


## No. Concentar el voto no tiene beneficios para el bloque.

En general: **Concentrar el voto en el partido más grande de un bloque ideológico NO beneficia de ninguna manera al bloque**.

Dejadme decirlo de primeras y así de claro.
Después os lo demuestro pero es tan flagrante que veo necesario decirlo así.

Tampoco hay nada mágico en la ley de D'Hondt que haga que tu voto valga más si votas a partidos grandes.

Tampoco es ahora en las Europeas, porque haya circunscripción única.
Es el caso general.
Estamos demasiado acostumbradas a las excepciones.

Las excepciones son:

- Cuando en una circunscripción se reparten pocos escaños (de 4 a 6).
Y en este caso el mayoritario no siempre es la mejor opción.
- Cuando consideramos las opciones sin posibilidades de alcanzar representación (¡¡no hablamos aqui de minoritarios con opción a representación!!)

## Contexto

De entrada, lo que sí se puede asegurar es que

> Concentrar el voto en un partido, beneficia, por supuesto, a ese partido.

Por eso lo repiten tanto en sus discursos. Tontos no son.

![Recortes de prensa](/images/2024-Europeas-concentracion-voto-recortes.svg)

- [Feijóo llama a concentrar el voto constitucionalista](https://www.elimparcial.es/noticia/269186/nacional/feijoo-llama-a-concentrar-el-voto-constitucionalista:-hoy-cs-es-el-pp-de-cataluna.html)
- [Sumar pide "concentrar el voto de la izquierda no nacionalista" en su candidatura](https://www.publico.es/politica/sumar-pide-concentrar-voto-izquierda-no-nacionalista-candidatura.html)
- [Sanchez llama a concentrar el voto en el PSOE para parar a VOX y el PP](https://www.europapress.es/nacional/noticia-sanchez-llama-concentrar-voto-psoe-alerta-apoyar-pp-vox-mismo-porque-pactaran-20240531213014.html)
- [El PSOE de Segovia llama a concentrar el voto en el Partido Socialista para reforzar la educación pública de calidad e impulsar la Formación Profesional](https://www.psoesegovia.es/el-psoe-de-segovia-llama-a-concentrar-el-voto-en-el-partido-socialista-para-reforzar-la-educacion-publica-de-calidad-e-impulsar-la-formacion-profesional/)
- [Molina pide "concentrar el voto en el PP" el 9J para que "Sánchez pierda el plebiscito sobre su persona"](https://www.europapress.es/andalucia/noticia-molina-pide-concentrar-voto-pp-9j-sanchez-pierda-plebiscito-persona-20240603135207.html)
- [Puigdemont, pujant als sondejos, insta a concentrar el vot](https://www.elnacional.cat/ca/eleccions/catalunya-2024/puigdemont-pujant-sondejos-insta-concentrar-vot-avisa-psc-es-quedara-pam-nas_1205429_102.html)
- [PSOE de Albacete: “El 9 de junio es imprescindible concentrar el voto en el PSOE porque es quien garantiza el desarrollo rural en Europa”](https://www.eldigitaldealbacete.com/2024/06/03/psoe-de-albacete-el-9-de-junio-es-imprescindible-concentrar-el-voto-en-el-psoe-porque-es-quien-garantiza-el-desarrollo-rural-en-europa/)
- [Aragonès reclama concentrar en ERC el vot catalanista i independentista](https://www.lavanguardia.com/encatala/20240510/9629460/aragones-reclama-concentrar-erc-vot-catalanista-i-independentista.html)
- [Aragonès crida a concentrar el vot d'esquerres i independentista per evitar un país de «casinos i asfalt»](https://naciodigital.cat/politica/aragones-crida-vot-esquerres-i-independentista-per-evitar-coalicio-han-manat-sempre_1930874_102.html)

Todas estas arengas se aprovechan de una percepción común, que como veremos no es real.
La realidad es que una transferencia de votos entre opciones políticas del mismo bloque ideológico:

- como máximo conseguiría un escaño más
- pero existe la misma probabilidad que suponga un escaño menos,
- y lo mas probable es que no altere para nada el resultado conjunto
- la ganancia o perdida es aleatoria y no tiene ningún tipo de proporcionalidad con el voto transferido.

Aquí no decimos las cosas por decir así que demostremoslo.

## Demostración

### Planteamiento

Como hemos explicado otras veces,
D'Hondt consiste, en el fondo, en establecer un precio de votos por escaño (que llamaremos P)
de modo que se repartan todos los escaños, sin que a nadie le que sobren votos para obtener uno más.
Lo que normalmente se explica de D'Hondt es el procedimiento para encontrar ese precio,
pero esta visión del objetivo que persigue nos da mucho más entendimiento de lo que está pasando.

![La parte semi transparente de las barras es el resto](/images/revote-pantallada-pricebars.png )

Según esto, todas las formaciones acabarán con un resto de votos sin escaño entre 0 y P-1.
En el [simulador](https://vokimon.github.io/revote), el resto es la parte semitransparente al final de las barras.

![La parte semi transparente de las barras es el resto](/images/2024-sobrantes.png )

Para comprobar si concentrar el voto consigue o no un beneficio para el bloque,
supondremos una situación inicial en la que se ha establecido un precio P por escaño.
Partiendo de esa situación inicial, plantearemos un trasvase de N votos de una formación a otra mayor.
¿mejora la representación de las dos en conjunto o no?

### Transfiriendo el precio de escaños enteros

La propia transferencia podría alterar el precio P, y esto hace que todo sea más complejo.
Por eso, empezaremos por un caso que no altera el precio:
una **transferencia de P votos**, es decir, **escaños enteros**.
La formación emisora perderá un escaño y la receptora lo ganará.
Como los restos seguirán siendo los mismos, nadie tendría votos para obtener más escaños de los que se habían repartido antes,
por lo que, como decíamos, no hará falta alterar el precio.

El escaño obtenido por la receptora simplemente compensa el escaño perdido por la emisora y la suma de escaño de ambos quedaría igual.
Podemos repetir el trasvase una y otra vez, mientras que tengamos votos a transferir, con el mismo resultado.
Aquí lo vemos en el simulador:

![Animación simulando transferencias de escaños enteros](/images/2024-Europeas-full-price-transfers.gif)

Aunque lo anterior solo se aplique a transferencias de votos múltiples exactos de P,
nos dice que según vamos convenciendo a gente de que hay que agregar el voto,
si en algún punto conseguimos que eso sume algun escaño para el bloque,
si seguimos convenciendo a gente, antes de llegar al siguiente múltiplo de P
ese efecto se revertirá.

En resumen, estamos haciendo transferencias muy grandes de votos,
convencimos a mucha gente de que hay que concentrar el voto,
pero no obtuvimos mejora alguna para el bloque, solo para el partido receptor.


### Transfiriendo fracciones del precio del escaño

En el anterior caso, ya hemos visto que,
moviendo un montón de votos, no hemos conseguido ningún beneficio.
Pero eso no quiere decir que no podamos obtenerlo entre múltiplo y múltiplo de P.
A simple vista, vemos que las barras que movíamos arriba,
tienen suficientes restos como para sumar un escaño nuevo si los juntamos.
Un escaño no es la [Bicoca] pero sería un beneficio a considerar.

[Bicoca]:https://es.wikipedia.org/wiki/Batalla_de_Bicoca

El problema es que, normalmente, no sabemos cuantos restos tendrá cada formación
y según los votos que trasvasemos, puede pasar que:

- Le quitemos demasiados a la emisora, pierda el voto que ganamos, y quede igual.
- No sumemos suficiente en la receptora y no llegue a sumar escaño, tambien quedaría igual
- Si se dieran las dos condiciones anteriores a la vez. En vez de ganar un escaño lo perderíamos.

¿Cómo de frecuente es cada caso?

El resultado depende de los restos que tenga cada partido y,
escaños y restos se comportan de forma parecida a una ruleta:

![Una ruleta](/images/2024-Europeas-spinning-wheel.gif)

Las **vueltas completas** que acaba dando serían los **escaños**.
El **sector** que acaba elegido serían los **restos**.
El **empuje** que le damos, o, más exactamente, la apreciación que tenemos de él, serían lo que dicen los **sondeos**.

Si hacemos trampas y empujamos flojo la ruleta,
tenemos bastante control de donde acabará la ruleta.
Esto quiere decir que con las formaciones para las que se preveen
pocos o ningún escaño, podríamos hacer predicciones de los restos.
Si empujamos más fuerte, igual podemos predecir las vueltas/escaños,
pero el sector final, los restos, se vuelve más impredecible.

Si no podemos predecir los restos finales,
lo mas honesto es considerar que todos los restos posibles, de 0 a P-1,
tienen la misma probabilidad (1/P).

Con un trasvase de N votos, la emisora pierde un escaño si su resto es menor que N.
La probabilidad de que esté en esa zona es la proporcion entre N y P.

![La zona de riesgo](/images/2024-Europeas-ZonaDeRiesgo.svg)

Y para que la receptora gane el escaño, le tienen que faltar N o menos votos para llegar al siguiente.
La zona esta en el otro lado pero tiene la misma proporción N/P.

![La zona de oportunidad](/images/2024-Europeas-ZonaDeOportunidad.svg)

Como los restos de ambas formaciones son independientes, podemos establecer el siguiente cuadro donde el area corresponde a la probabilidad.

![Co-ganancia cero](/images/coganancia-zero.svg)

En la zona amarilla, no nay cambios en el resultado, todos matienen sus escaños y el bloque se queda igual.
En la zona azul, ambos partidos estaban en la zona critica para N votos, así que uno gana y otro pierde, pero el bloque queda igual, como en el trasvase de P votos.

En las zonas la roja y verde, el bloque gana o pierde un escaño, porque un partido estaba en la zona crítica y el otro no.
En todo caso, las áreas son equivalentes, así que son igual de probables.

Para este viaje no hacian falta alforjas.
Por mucha gente que convenzas de que concentre el voto, el resultado para el bloque va a ser el mismo escaño arriba o, importante, escaño abajo.
Y no es porque sean Europeas.
Este es el comportamiento normal de D'Hondt.
Aunque exista el mito de que D'Hondt hace que el voto de los mayoritarios "valga más".

Quizás la impresión venga de que el mismo resto de votos es, en porcentaje del voto recibido, mayor en pequeños que en grandes,
pero 500 votos tienen la misma capacidad de quitar o añadir escaño en grandes que en pequeños.

## Caso especial: Pocos escaños

Siguiendo el símil de la ruleta, si empujamos flojo para que dé pocas vueltas, es más facil predecir lo que saldrá.
Esto pasa en convocatorias en que se reparten pocos escaños que no es el caso de las Europeas.
También pasa con las formaciones con poca o nula representación.

Podemos usar esa nueva información para ajustar el tiro: Si probablemente estés en la zona crítica entre dos escaños, puede beneficiar recibir un trasvase.
Y si no tienes posibilidades de alcanzar el primer escaño, sintiendolo mucho pero, con lógica de bloques, tus votos pueden ser útiles al bloque en otro partido.

La suposición que haciamos antes de que todos los restos son igualmente probables, se rompe en los minoritarios.
Normalmente unos pocos partidos tienen más de medio escaño y el resto tienen muy poquitos votos.
Siguiendo distribuciones parecidas a [Zipf](https://en.wikipedia.org/wiki/Zipf%27s_law)/[Pareto]() o [exponencial](https://en.wikipedia.org/wiki/Exponential_distribution).

![Distribución Pareto](https://upload.wikimedia.org/wikipedia/commons/1/11/Probability_density_function_of_Pareto_distribution.svg)


El problema es que **tenemos tan interiorizado el caso del minoritario que no llega en las generales en las provincias pequeñas que pensamos que siempre es así.**
Los partidos grandes de cada bloque utilizan esta percepción para arrimar el ascua a su sardina.

## Coaliciones electorales, la agregación efectiva de voto, aunque en Europeas... pse...

Como ya vimos en [otro articulo](/posts/2014-12-05-llistes-dunitat-nacional-confluencies-i-daltres-animals-politics.html)
juntando listas con representación en una coalición,
estadísticamente podemos esperar ganar medio escaño por circunscripción y por lista añadida,
por la suma de restos.

Con algunos peros:

- El efecto no se limita al matemático: Depende de lo que ilusione o desmotive la fusión a los votantes
- Estamos hablando de medio escaño, relativicemos.
- Si lo que fusionamos no son listas con representación (extraparlamentarias) el efecto es más limitado que medio escaño, puesto que los restos que aportan son menos
- **Es un efecto que se multiplica por cada circunscripción y en europeas solo hay una**

Una vez que se proclaman las listas concentrar el voto no tiene el mismo efecto que la coalición,
puesto que alguien votará a la otra lista, y generará esos restos que si hubiera coalición se sumarían.

En europeas este tipo de coalición tiene mucho sentido en partidos territoriales
que en otras convocatorias se benefician de tener el voto concentrado en circumscripciones.
Como han hecho Esquerra, Bildu, BNG...
Como NO han sabido hacer Junts, PNV y Coalicion Canaria.
Y como siempre hacen desastrosamente los Extremaduristas que este año van en 3 listas diferentes.


## El origen de la falsa percepción

Hay varias pistas falsas que nos llevan a pensar que agregar el voto en el mayoritario es bueno.

### "Podríamos haber sumado estos restos"

El retorno del Capitan "A Posteriori".

![Capitan A Posteriori](/images/capitan-aposteriori.png)

Cuando ya se tienen los resultados, sucede que a menudo ves que los restos de dos opciones juntas podrían sumar un escaño más.
Además, si son opciones de tu bloque, duele, lo que lo hace más memorable.
En cambio, las muchas otras veces en que esto no pasa, no son tan memorables pero son más.

Cuando se ven los restos que podrían sumar,
el Capitan A Posteriori dice: "Tendríamos que haber movido voto a un solo partido".
Pero mientras no haya una coalicion electoral,
y mientras que haya gente que siga votando a los dos partidos,
los dos restos pueden estar en cualquier punto entre un escaño y el siguiente.
Y eso implica que el movimento de votos no tienen asegurada ninguna ganancia
en el bloque: puede sumar, quedarse igual o incluso restar.

### "La proporción de votos por escaño es mayor en los pequeños"

Para mostar los fallos del sistema electoral,
a menudo, se menciona la proporción entre voto recibido y escaños obtenidos
para señalar lo injusto del sistema electoral, y es un planteamiento correcto.
Pero a menudo esa forma de expresarlo nos lleva a pensar que, realmente, tu voto si votas a un minoritario vale menos.

¿De dónde sale esa desproporción y porqué no es correcto trasladarla a la capacidad de tu voto?

Por como funciona D'Hondt,
todos los partidos con representación en una circunscripción tendrán un resto entre 0 y P-1.
En media les sobrará medio escaño.
Ese medio escaño supone una parte proporcional de los votos más importante para los partidos con pocos escaños que para los que tienen muchos.

Un ejemplo práctico: Imagina que sale un escaño vale 100.000 votos.
A un partido con 10 escaños que le sobre medio, le sale un escaño a 105.000 votos.
A un partido con 2 escaños que le sobre también medio, le sale a 125.000 votos.

Dicho así parece que haya que juntar más votos para que salga un escaño del pequeño.
Pero la verdad es que 50.001 votos, consiguirían el siguiente escaño tanto si van al grande como si van al pequeño.


## Conclusión

- No, D'Hondt no hace que tu voto valga más si votas a un mayoritario.
Dentro de cada circunscripción 100 votos a uno pequeño valen lo mismo que a uno grande.
- No, esto no es solo para las Europeas, es el caso general
- Si quieres hacer voto estrategico de bloque, la clave no está en si es más grande o pequeño, sinó si esta en zona de riesgo/oportunidad o no.
Esto es más facil de predecir cuando la formaciones recibe pocos escaños, porque es pequeña o porque hay pocos a repartir.
- Si, trasvasar los votos a los extraparlamentarios sin opciones de representación puede tener efectos buenos (aunque poquitos) para el bloque
- No, lo anterior no es aplicable a los pequeños con representación solo a extraparlamentarios sin opciones.











