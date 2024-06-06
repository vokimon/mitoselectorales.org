---
title: Europeas 2024: ¿Hay que concentrar el voto?
date: 2024-06-03 09:03
author: David García Garzón
tags: D'Hondt, Europeas, Lógica_de_Bloques
status: published
cover: images/hay-que-concentrar-el-voto.png
---

<!-- PELICAN_BEGIN_SUMMARY -->

Europeas 2024.
Los partidos insisten con el mensaje: «Hay que concentrar el voto en nuestro partido para que le vaya bien a tal o cual bloque ideológico».
No son tontos... ni sinceros.
Es mentira que funcione así y te lo explicamos visualmente en este artículo.

<!-- PELICAN_END_SUMMARY -->

## No. Concentar el voto no tiene beneficios para el bloque.

En general: **Concentrar el voto en el partido más grande de un bloque ideológico NO beneficia de ninguna manera al bloque**.

Dejadme decirlo de primeras y así de claro.
Después os lo demuestro pero es tan flagrante que veo necesario decirlo así.

No hay nada mágico en la ley de D'Hondt que haga que tu voto valga más si votas a partidos grandes.

No es ahora en las Europeas, porque haya circunscripción única.
Es el caso general.
Estamos demasiado acostumbradas a las excepciones.

Las excepciones son:

- Cuando en una circunscripcion se reparten pocos escaños (de 4 a 6).
Y en este caso el mayoritario no siempre es la mejor opción.
- Cuando consideramos las opciones sin posibilidades de alcanzar representación (¡¡no hablamos aqui de minoritarios con opción a representación!!)

## Qué está pasando

De entrada, lo que podemos asegurar es que concentrar el voto en un partido, beneficia, por supuesto, a ese partido.
Por eso lo repiten tanto.
Que no, que no son tontos.

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

Todas estas llamadas se aprovechan de una percepción que tenemos que es eso, una percepción.

La realidad es que una transferencia de votos entre opciones políticas del mismo bloque ideológico:

- apenas puede suponer un escaño más para el bloque (en una circumscripción)
- lo grave es que existe la misma probabilidad que suponga un escaño menos, y,
- lo mas probable es que no altere para nada el resultado conjunto.

Aquí no decimos las cosas por decir así que demostremoslo.

## Demostración

Como hemos explicado otras veces, D'Hondt en el fondo consiste en fijar un precio de votos por escaño (P) para que se repartan todos los escaños, sin que a nadie le que sobren votos para obtener más.

![La parte semi transparente de las barras es el resto](/images/revote-pantallada-pricebars.png )

Todas las formaciones tendrán un resto de votos sin escaño entre 0 y P-1.
En el [simulador](https://vokimon.github.io/revote), el resto es la parte semitransparente al final de las barras.

![La parte semi transparente de las barras es el resto](/images/2024-sobrantes.png )

Partamos de una situación de referencia en la que se ha establecido un precio P por escaño.
Planteemos: ¿Qué pasa si trasvasamos de N votos de una formación emisora a otra receptora del mismo bloque ideológico? ¿Mejora la representación del bloque en conjunto o no?

Primero el caso sencillo: **transvasar justo el precio de un escaño, P votos**.
La emisora perderá un escaño y la receptora lo ganará.
Los restos siguirán siendo los mismos, por lo que no habrá que cambiar el precio.
La suma del bloque quedaría exactamente igual.

Con votos suficientes en la emisora, podemos repetir con paquetes de P votos y pasará lo mismo.
Si movemos 10 escaños enteros, seguirá sin beneficio de bloque.

¿Igual tenemos algún beneficio trasvasando fracciones de P?

Intuitivamente podemos ver que juntando restos de dos formaciones a veces se podría sumar un escaño.
Pero ¿realmente son restos lo que quitamos de la emisora? ¿son suficientes para sumar en la receptora? No sabemos de cuantos restos disponen cada una.

Los restos se comportan como una ruleta.
Por la fuerza que lleva se podría prever las vueltas que darás, que serían los escaños.
Predecir el sector final es más complicado.
El sector serían los votos restantes.

![Una ruleta](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXIxZjIzd2V1MjAxaGhqMnd0YmZhNWJvMTNlendjYnEyMXVtd3FyeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohhwiunVgYqfVYVEs/giphy.gif)

Ante nuestra falta de información, la estimación más honesta es que todos los restos posibles entre 0 y P-1 tienen la misma probabilidad 1/P.
No aplicaría cuando le damos flojo a la ruleta (0 o 1 escaños) pero dejamos para después ese caso.

Con un trasvase de N votos, la emisora pierde un escaño si su resto es menor que N.
La probabilidad de que esté en esa zona es la proporcion entre N y P.

![La zona de riesgo](/images/2024-Europeas-ZonaDeRiesgo.svg)

Para que la receptora gane el escaño, le tienen que faltar N o menos votos para llegar al siguiente.
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

Siguiendo el símil de la ruleta, si apenas da vueltas es más facil predecir el sector final.
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

## Conclusión

- No, D'Hondt no hace que tu voto valga más si votas a un mayoritario.
Dentro de cada circunscripción 100 votos a uno pequeño valen lo mismo que a uno grande.
- No, esto no es solo para las Europeas, es el caso general
- Si quieres hacer voto estrategico de bloque, la clave no está en si es más grande o pequeño, sinó si esta en zona de riesgo/oportunidad o no.
Esto es más facil de predecir cuando la formaciones recibe pocos escaños, porque es pequeña o porque hay pocos a repartir.
- Si, trasvasar los votos a los extraparlamentarios sin opciones de representación puede tener efectos buenos (aunque poquitos) para el bloque
- No, lo anterior no es aplicable a los pequeños con representación solo a extraparlamentarios sin opciones.
