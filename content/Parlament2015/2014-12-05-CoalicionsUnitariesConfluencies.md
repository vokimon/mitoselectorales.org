title: Llistes d'unitat nacional, confluències i d'altres animals (polítics)
author: David García Garzón
tags: Parlament, Coaliciones, D'Hont
cover: images/llistaunitaria-sumarestos.png
status: published

Tothom ha escoltat les propostes de ERC i CiU de com anar a unes eventuals eleccions plebiscitàries.
Junts o barrejats.
Un dels arguments que s'han fet servir per fer una candidatura unitària
és que es veuria beneficiada pel sistema electoral.
Jo em pregunto, segur?
Anem a fer els deures per ells, farem l'anàlisis electoral.

Sent honest, cal dir que tinc un cert biaix:
Personalment em sembla una bejenada democrática
que es vulgui diluir els matissos polítics de la gent que vota.
A més opcions, més fàcil de trobar una opció amb la que comulguis amb més coses.
Si juntes en l'eix nacional, treus als ciutadans capacitat de decidir sobre l'eix social,
i això simplificant les opcions es puguin simplificar en dos únics eixos.

Així doncs, malgrat que intento recolzar-me en les matemàtiques,
otorgo la responsabilitat jutjar l'efecte del meu biaix al lector.

Realment el sistema electoral afavoriria una llista conjunta?

## La hipòtesis de simplement sumar (ni restar, ni multiplicar)

Hi ha factors en l'efecte d'una llista conjunta que són molt poc previsibles
i que cal estimar de forma molt subjectiva.
No tothom que votés a una opció per separat votaria la conjunta i a l'inrevés.
Per això el que faré és primer fer la hipòtesi de que
els vots a les diferents opcions en una llista conjunta simplement s'agregarien,
sense foragitar votants, ni atreure nous votant.
Una hipòtesi molt improbable, però que dibuixa un escenari base
sobre el que fer després les nostres estimacions subjectives sobre els fluxos electorals que es puguin donar.


## Efecte de la suma de restes

Sovint s'explica D'Hondt descrivint el procediment que cal seguir per repartir els escons,
i aquest procediment sovint enmascara la comprensió del s'està fent:
**Una subasta que estableix el preu mínim en vots per cada escó**
tal que, si reparteixes tots els escons a aquest preu, a cap opció li queden vots per tenir-ne més.

Una conseqüència d'aquesta definició és que, un cop establert aquest preu mínim,
a totes les formacions els sobrarà un nombre de vots
entre 0 i el preu mínim (menys 1) per obtindre el següent escó.

Evidentment, si les formacions s'uneixen, aquests vots sobrants
podrien sumar per obtenir un nou escó que no obtindrien per separat.

Si considerem les formacions que clarament obtindran representació,
com ho son CiU, ERC, ICV...
estadísticament el número de vots sobrants tenen la mateixa probabilitat
de ser 0, 1, 40, o el preu minim menys 1.
És el que s'en diu una distribució de probabilitat uniforme
que seria la corba plana de la gràfica.

![Distribució de probabilitat de guanyar escons adicionals sumant restos]({static}/images/llistaunitaria-sumarestos.png)

[Codi Python per generar la gràfica]({static}llistaunitaria.py)

Quan sumes els sobrants de N partits amb representacio,
el resultat són distribucions que ja no són uniformes.
En general, el realme del que és possible estaria entre 0 i N-1 escons addicionals,
però, la situació més esperable serien (N-1)/2 escons.

Per exemple, com es pot veure al graf,
amb dos formacions hi ha una probabilitat del 50%
d'obtenir 0 escons i 50% d'obtenir 1 escó.
Amb tres formacions, lo més probable, 67%, és que sumi un escò
però també podria obtindre cap o 2.

És a dir, la suma dels sobrants afegirien per cada circumscripció:

- 2 formacions: 0-1 (igual de probable 0 o 1)
- 3 formacions: 1
- 4 formacions: 1-2 (igual de probable 1 o 2)
- 5 formacions: 2

Com aquest mateix efecte passa a cada circumscripció, cal multiplicar per quatre.

**En resum, cada formació que juntem, de les que normalment obtenen representació en les quatre circumscripcions,
aporta 2 escons addicionals per suma de restos.**

ERC+CiU obtindria 2 escons addicionals i ERC+CIU+CUP obtindria 4.
No és gaire però podria ser decissiu.


## Sumant restes de formacions amb perill de quedar fora

Hi ha formacions que incorporades a la candidatura unitària
tenen un efecte a la suma dels restos més gran del normal.
Es tracta de les candidatures que, a Barcelona província, i només a Barcelona,
tenen perill de no arribar al llidar del 3% que marca la llei.

Això és una singularitat que es dona a les autonòmiques catalanes
i només a la província de Barcelona perquè el preu de l'escò,
que normalment és lleugerament superior al 1%, està molt per sota del llindar del 3%.
Així una formació es pot quedar fora del repartiment tenint vots
per 2 o gairebé 3 escons.

Això vol dir que incorporar a Barcelona,
una candidatura amb perill de quedar-se
sense representació i amb posibilitats de tenir-ne,
assegura 2 o 3 escons més a la candidatura unitària
que d'una altra manera es podrien perdre.

També és diferent l'efecte de les formacions marginals.
En aquestes formacions, el vot residual, que és tot el vot rebut,
no respon a una distribució uniforme,
sinó que tendeix a estar concentrat a la part baixa.
Sumaran, però una part molt petita.

## Repartiment desproporcional de les fraccions per D'Hondt

Adalt he suposat que el preu per escó no varia pel fet de agregar les candidatures.
Pero no és així.
D'Hondt fa que les candidatures amb més vots estiguin sobrerepresentades.
Però aquesta tendència mal entesa, fa que sovint treguem conclusions errònies
com les que s'han vist als mitjans aquests dies.
Analitzem-ho.

D'on ve aquesta sobrerrepresentació?
Si poguessim repartir trossos d'escons podríem fer repartiment totalment proporcional als vots.
Una formació podria tindre 7'3 escons i una altra 2'7.
Els sistemes de repartiment, difereixen en com es reparteixen els escons trossejats per tenir escons sencers.
Un sistema com el de Hamilton, més proporcional,
repartiria els escons a les formacions que tenen més decimals.
És a dir, que 2'7 s'emportaria l'escò perque està més a prop del 3 que 7'3 del 8.

D'Hondt, en canvi, el que fa es baixar el preu de l'escó fins que es reparteixen tots.
Si baixem el preu de l'escò un 1%, un formació amb 10 escons es com si li sumessis als restos un 11% del preu d'escó,
en canvi una formació amb 3 econs només li pujaries un 4%.
És possible que una formació minoritària obtingues l'escó sobrant (si ja tingues un 96% del següent escó), però és molt menys probable.

A un nombre do vots fix:
- Preu minim: quan totes les candidatures tenen molts restos 1/(E+C)
- Preu maxim: quan totes les candidatures tenen minims restos 1/C




Considerem que a un repartiment hi han hagut _V_ vots i _E_ escons a repartir.
El preu màxim sera `P=V/E` vots per escó.
Assignant escons a aquest preu, una formació que ha obtingut _v_ vots obte _e_ escons i li sobren _r_ vots.
Quin factor _f_ ha de reduir el preu la llei D'Hondt per que s'obtingui exactament el següent escò?

$$ v = e · p + r  = (e+1) · p · f $$
$$ e + r/p = (e + 1) · f  $$
$$ f = { e + r/p \over  e + 1}  $$

$$ v = e · p + r  = (e+1) · p · f $$


f = (e·p + r) / (e·p + p)

f = (e + r/p) / (e+1)


v = e · p + r = (e+1) · (p - d)

ep+r = ep -ed +p -d
r = -ed +p -d

d = (p-r) / (e+1)
d/p = (p-r)/p / (e+1)


Quants es el minim d'escons de restos que es reparteixen?

Descartant el cas infinitament improbable que totes les candidatures recollissin l'escó just per tenir el darrer escó ($1\over {p^C}$),
la següent opció molt més probable es que totes les formacions tinguèssin alguna part d'un sól escó.







Quants escons extres podrien acabar caient en una formació?
Doncs normalment un.
És possible que es donin més d'un però, per a que això passi
la força majoritària hauria de tenir uns percentatges de vots tals que
ja no ens treuria la son un o dos escons més o menys.

Així doncs, D'Hondt reparteix un escó extra
a cadascuna de les formacions majoritàries a cada circumscripció.
I aquí està la clau!!
Donat que CiU i ERC són ara mateix les dues formacions majoritàries,
serien les primeres en rebre els escons de sobrerrepresentació.
Dos escons per circumscripció. Total: 8 escons.
I si van juntes, com només són una formació,
només reben 4 escons, un per circumscripció.


## Resumint els efectes de la llei electoral

- Suma de restos:
	- Una candidatura amb representació a totes les circumscripcions, que s'agregui a la candidatura unitària sumaria 2 escons
	- Una candidatura en risc de no arribar per separat a Barcelona al llindar del 3%, a la candidatura 2 i 3 escons
- Sobrerrepresentació per D'Hondt
	- Cada candidatura majoritaria a una circumscripció implica perdre 4 escons


En resum, si considerem que la unió de candidatures no crea
moviment de vot ni en positiu ni en negatiu, tenim que:

- Separats ERC + CiU: 0 de restes + 8 de D'Hondt = 8 escons extra
- Junts ERC + CiU: 2 de restes + 4 de D'Hondt = 6 escons extra

Matemàticament perdrien 2 escons!

Si fiquem a l'equació CUP, suposant que CUP
és de la meitat cap abaix entre les formacions amb representació i no té bonificació D'Hondt:

- Separats ERC + CiU + CUP: 0 de restes + 8 de D'Hondt = 8 escons extra
- Junts ERC + CiU + CUP: 4 de restes + 4 de D'Hondt = 8 escons extra

Sorprenentment la llei electoral els deixa igual.

Altres fórmules podrien ser més beneficioses,
sobretot, com hem dit agregant partits amb risc de quedar-se fora.
Però la llei D'Hondt no serà més beneficiosa del que ja és
i només tindra l'efecte dels restes que s'agregarien.


## Moviment de vot (o no vot) pel fet de juntar-se

Amb la base del que ens dona la llei electoral,
que ho pinta una mica magre per una llista unitària que agregui les dues opcions majoritàries.
cal analitzar els fluxes entre les diferents opcions de vot o de no-vot.

Per fer aquest anàlisis, la clau està en identificar els perfils dels votants
que canviarien el seu vot o no-vot i després intentar quantificar el seu número.

- Quin perfil de votant de un partit deixaria de votar a la llista unitària si en ella van els partits que hi van?
- Quin perfil de votant que no votaria als partits de la llista, passaria a votar la llista?

Subjectivament, a mi em fa la impressió que el primer cas domina sobre el segon.

El fluxe negatiu d'una llista independentista unitària crec que seria important.
Molta gent que votaria per separat a CUP, ICV o ERC no voldria votar al Mas de les retallades.
No crec que sigui tant important en el cas de votants de CiU respecte la inclusió dels altres.

I el fluxe positiu, d'on hauria de vindre?
No vindrà pas tampoc del votant unionista del PP i C's.
El fluxe entre opcions independentistes no varia l'efecte.
Només pot vindre de l'abstenció independentista i del votant que,
tot i ser independentista, prioritza l'eix social.
L'abstenció independentista no crec que sigui significativa
en unes eleccions plantejades com a plebiscitàries.
I la capacitat d'atreure els *independentistes socials*
està bastant condicionada a la generositat que es tingui en aquest eix
a l'hora de plantejar la unitat.

En tot cas, l'efecte amunt i avall de tot plegat, ha de poder compensar-se
amb l'efecte clarament contrari de la llei electoral envers una llista unitària.
O sigui, en global, crec que una candidatura unitària és electoralment contraproduent
pel bloc independentista, a part de que és contrari a la democràcia,
en castrar la possibilitat de que els ciutadans es posicionin també
en altres aspectes de la vida i, molt important,
quines serien les bases sobre les que construir aquest nou país.






