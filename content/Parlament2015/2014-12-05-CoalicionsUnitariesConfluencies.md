---
title: Llistes d'unitat nacional, confluències i d'altres animals (polítics)
author: David García Garzón
tags: Parlament, Coaliciones, D'Hont
cover: images/llistaunitaria-sumarestos.png
covercaption: Probabilitat d'afegir escons en una circumscripció amb la suma de candidatures
status: published
---

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
Amb tres formacions, lo més probable, 67%, és que sumi un escó
però també podria obtindre cap o 2.

És a dir, la suma dels sobrants afegirien **per cada circumscripció**:

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
i només a la província de Barcelona perquè el preu de l'escó,
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

## Mite: D'Hondt afavoreix l'agregació de candidatures

D'Hondt fa que les candidatures amb més vots estiguin sobrerepresentades.
Una candidatura agregada estaría més sobrerepresentada encara?
Doncs sí, però, no.
Es a dir, estaria més sobrepresentada, sí,
però treient la suma dels restos que explicavem abans,
**el que fa es sumar les sobrerepresentacións de les dues candidatures originals.**

Ho pots comprobar empíricament amb l'eina [enVote]({filename}/pages/envote.md),
agafant qualsevol parell de candidatures i fent una transferència total d'una cap a l'altra.
Comprovaràs que **no hi ha més guany del que poguem preveure amb la suma de restos**.

Per entendre perquè és així cal entendre d'on ve la sobrerrepresentació de D'Hondt.

Si poguessim escuarterar els polítics, podríem fer un repartiment totalment proporcional als vots.
Una formació podria tindre 10'3 escons i una altra 2'7.
Els sistemes de repartiment, difereixen en com es reparteixen els escons trossejats per tenir escons sencers
i no haver de fer cap canisseria.

Per exemple, el sistema [Hamilton](https://ca.wikipedia.org/wiki/M%C3%A8tode_de_Hamilton),
més proporcional que el que tenim,
repartiria els escons a les formacions que tenen els restos més grans.
És a dir, que 2'7 s'emportaria l'escó perque està més a prop del 3 que ho està 10'3 de l'11.

D'Hondt, en canvi, el que fa es baixar el preu de l'escó fins que es reparteixen tots els escons.
Si baixem el preu de l'escó un 1%, una formació amb 10 escons afegeix als seus restos un 1% per escó, el 10%.
En canvi, una formació amb 2 escons només li afegiries un 2%.
Potser la minoritària tenia 97% i amb el 2% ja arriba al nou preu de 99% per escó,
però pots veure que si tenim molts escons sobrants, el repartiment acabarà sent proporcional al tamany de la candidaura.
En contra Hamilton reparteix a cada candidatura només un o zero escons sobrants.

Llavors, perque no es beneficia d'això una coalició?
Perque la proporcionalitat en el repartimen dels escons sobrants ja s'estava aplicant per separat,
i l'únic efecte que té, són els esmentats restos de vots sense esco.


## Resumint la suma matemàtica de vots

- El que afecta es la suma de restos:
	- Una candidatura amb representació a totes les circumscripcions, afegeix a la candidatura unitària 2 escons extres (mig per circumscripció)
	- Una candidatura en risc de no arribar per separat a Barcelona al llindar del 3%, a la candidatura 2 i 3 escons per Barcelona

En resum, si considerem que la unió de candidatures no crea
moviment de vot ni en positiu ni en negatiu, tenim que:

- Junts ERC + CiU: 2 escons de restes

Si fiquem a l'equació CUP, suposant que CUP
és de la meitat cap abaix entre les formacions amb representació i no té bonificació D'Hondt:

- Junts ERC + CiU + CUP: +4 escons de restes +2 de la CUP a Barcelona que es podrien perdre si no arriben al llindar 


## Possibles moviments pel fet de juntar-se

Aixì doncs tenim quantificat l'avantatge de la coalició si no hi haguessin moviments electorals.
Per fer l'anàlisi complert necessitem evaluar quins moviments hi hauria i comparar-ho.
Cal identificar els perfils que podrien moure la seva opció i comparar-ho amb els escons d'avantatge.

En vots quin és aquest avantatge:

Depén del preu de l'escó.
El tenim limitat per dalt per l'expresió $$ Preu_{max} = {votants \over escons} $$

I el preu mínim per:
$$ Preu_{min} = {votants \over escons + candidatures } $$

El preu típic tenint en compte seria:
$$ Preu_{min} = {votants \over escons + candidatures/8 } $$


Per fer aquest anàlisis, la clau està en identificar els perfils dels votants
que canviarien el seu vot o no-vot i després intentar quantificar el seu número.

- Què faran els **actuals votants independentistes**
	- En cas de coalició: Es perdrien els que rebutgen les altres candidatures
		- Democristians que rebutjin mesures socials o l'aument d'impostos
		- Socials que rebutjin les retallades i la corrupció de CiU
	- Una formació independentista fora de la coalicio podria recollir aquest vot.
	- En cas de anar separats: Es perdrien els que es desmobilitzin per la contesa interna entre els partits.
- Què faran els **actuals abstencionistes**
	- Una candidatura conjunta que diluís els partits podria atreure els que rebutgen les dinàmiques de partit
	- Hi ha poc independentista que no estigui mobilitzat
- Què faran els votants de candidatures no independentistes
	- Aquest perfil si que es significatiu en número
	- Aquests votants estan en l'àmbit de l'esquerra no independentista
	- Molt improvable trobar-los als votants del PP i C's
	- Aquest perfil és molt probable que valori negativament una coalició amb la dreta catalana de les retallades. 
	- Els que vinguin, probablement vindrien més si no hi ha coalicio

El guany matemàtic es prou petit com per a que aquests moviments el malmetin.

Potser és el guany que es requereix per obtindre la majoria sense la CUP (o amb la CUP).

El que tinc clar es que per donar força a un eix polític, el nacional,
els ciutadans tindran menys opcions per escollir d'altres eixos, i en concret el social.

Potser la gent que vota a Esquerra que te més present l'eix social i
que no volen a MAS aniran a parar a la CUP.

Qui ho sap.

