title: reVote: Simulador online de flujos electorales
description: Herramienta libre para simular flujos entre fuerzas políticas a partir de escenarios reales
date: 2019-01-30 00:00
tags: Simulador
status: published
---

![Logo reVote](/images/revote.png){style=float:right;padding:20px}

`reVote` es una aplicación web que,
partiendo de escenarios electorales reales o hipotéticos,
permite simular flujos de electores
entre diferentes opciones,
incluyendo opciones de no-voto.

[¡Úsala!](https://vokimon.github.io/revote)  &nbsp;&nbsp;&nbsp;
[¡Modifícala!](https://github.com/vokimon/revote)  &nbsp;&nbsp;&nbsp;
[¡Tradúcela!](https://github.com/vokimon/revote/tree/master/src/i18n) 

[![Pantallada reVote](/images/revote-pantallada-pricebars-full.png)](/images/revote-pantallada-pricebars-full.png)

## Historia

reVote se basa en una herramienta de escritorio,
[enVote], también libre,
que se desarrolló en el contexto de
la acampada de indignad@s de Sant Joan Despí
para poder dar respuesta de forma 
más ágil a las muchas dudas que teníamos sobre el 
funcionamiento del sistema electoral. Las normas 
pueden estar claras, pero a veces deducir los 
efectos de esas normas es complejo.

[enVote]:{filename}envote.md

## Funcionalidades


Los puntos fuertes del programa son:

- Tiene en cuenta abstención, voto en blanco y nulo como opciones
- Se pueden manipular los datos haciendo transferencias de una opción a otra
- Viene con casos hechos, reales, encuestas y de exploracion, y es fácil añadir otros.
- Visualiza claramente como se comportan esas transferencias con la Ley de Hondt y el umbral del 3% sobre el voto válido
- Se limita a simular una circunscripción que es donde el voto de cada ciudadano tiene efecto

Uso
---

Justo debajo del título, tienes un desplegable y dos botones
para ir cambiando de escenario base.

[![Control de escenario](/images/revote-pantallada-scenario.png)](/images/revote-pantallada-scenario.png)

Puedes modificar el escenario con los controles
que hay abajo a la derecha.
Sirven para hacer trasvase de votos de una opcion a otra.
Se puede seleccionar origen y destino con los desplegables
o mucho más práctico, a veces, se puede clickar con los botones derecho o izquierdo
a una opcion en cualquier gráfico (tartas, cocientes, barras...).

[![Control de transferéncia](/images/revote-transfer-widget.png)](/images/revote-transfer-widget.png)

[![Hemiciclos](/images/revote-pantallada-hemiciclos.png){max-heigth=5em}](/images/revote-pantallada-hemiciclos.png){style='max-heigth:5em;float:right;padding-left:1em'}

Las tartas de la parte izquierda representan, de arriba a abajo,
como cambia progresivamente las proporciones desde la opción
de los electores, incluyendo no-voto, hasta el reparto final.

* Proporción de cada opción, considerando el censo completo (opciones de voto y no-voto)
* Proporción considerando solo candidaturas
* Reparto hipotético usando una ley más proporcional (Hamilton) y sin umbral.
* Reparto de escaños según la ley de Hondt (la legal)

A la derecha arriba estan las estadísticas del escenario.

A la derecha en el centro puedes escoger el centro puedes escoger
varias visualizaciones con las pestañas.

El **tab `Precio`** muestra barras que representan el voto directo.
Pero tiene una doble escala móbil que muestra el precio variable
del escaño cuando cambiamos el escenario.

[![Vista de precio móbil de reVote](/images/revote-pantallada-pricebars.png)](/images/revote-pantallada-pricebars.png)

La gracia de la vista es visualizar como los flujos alteran el precio del escaño
y poder comparar visualmente ese precio con el umbral electoral.
La parte tanslúcida al final de cada son los votos que no han servido para sumar escaño.


El **tab `Cocientes`** muestra el resultado del reparto de D'Hondt
por el procedimiento habitual, la subasta de cocientes:

[![Vista de cocientes del reVote](/images/revote-pantallada-quocients.png)](/images/revote-pantallada-quocients.png)

* Los cocientes con el fondo azul son los que han obtenido escaño.
* Los cocientes con un fondo azul más oscuro son los escaños extra por D'Hondt.
* Los cocientes con borde rojo son los cocientes extra que se hubieran repartido por Hamilton.
* Los cocientes con letra roja son los que están mas cerca de obtener o perder un escaño.
* Los cocientes de las candidaturas fuera del umbral y las opciones de no voto se ven de color gris
* Los cocientes con fondo gris son cocientes que si fueran una candidatura o no hubiera umbral habrían obtenido un escaño


