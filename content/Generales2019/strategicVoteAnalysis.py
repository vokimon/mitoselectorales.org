#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

from sympy import (
	symbols,
	Eq,
	Lt,
	Gt,
	solve,
	)

# Definimos los símbolos
(
	erc1, erc2, erc3, # votos a 1r, 2o y 3r candidatos de ERC al senado
	jxc1, jxc2, jxc3, # votos a 1r, 2o y 3r candidatos de JxC al senado
	fr, # votos al senador de FR
	# Perfiles de votantes
	x_300, # Voto monocolor a los senadores de ERC
	x_030, # Voto monocolor a los senadores de JxC
	x_001, # Voto monocolor al senador de FR
	x_100, # Voto no indepe a ERC
	x_010, # Voto no indepe a JxC
	x_210, # Voto principal ERC, ayuda a JxC
	x_120, # Voto principal JxC, ayuda a ERC
	x_201, # Voto principal ERC, ayuda a PR
	x_021, # Voto principal JxC, ayuda a PR
	x_111, # Voto repartido
	A, B, D,
) =  symbols('''
	erc1 erc2 erc3
	jxc1 jxc2 jxc3
	fr
	x_300
	x_030
	x_001
	x_100
	x_010
	x_210
	x_120
	x_201
	x_021
	x_111
	A B D
''',)# real=True, positive=True, nonzero=True)

incognitas = [x_300, x_030, x_210, x_120, x_201, x_021, x_111, x_001, x_100, x_010, A, B, D]

constants = dict(
	erc1 = 928722,
	erc2 = 676858,
	erc3 = 577003,
	jxc1 = 444077,
	jxc2 = 289012,
	jxc3 = 218531,
	fr = 152113,
	congress = 1112142,
	#x_010 = 60000,
	#x_100 = 30000,
)

#     	300	210	201	111	001	021	120	030
# ERC3	1	0	0	0	0	0	0	0
# ERC2	1	1	1	0	0	0	0	0
# ERC1	1	1	1	1	0	0	1	0
# FR  	0	0	1	1	1	1	0	0
# JXC1	0	1	0	1	0	1	1	1
# JXC2	0	0	0	0	0	1	1	1
# JXC3	0	0	0	0	0	0	0	1

import sys
print(sys.modules[__name__])

equations = [
	Eq(x_300, erc3), # Perfiles que dan votos al tercero de erc
	Eq(x_030, jxc3), # Perfiles que dan votos al tercero de jxc
	Eq(x_300 + x_210 + x_201, erc2), # Perfiles que dan votos al segundo de erc
	Eq(x_030 + x_120 + x_021, jxc2), # Perfiles que dan votos al segundo de jxc
	Eq(x_300 + x_210 + x_201 + x_120 + x_111 + x_100, erc1), # Perfiles que dan votos al primero de erc
	Eq(x_030 + x_120 + x_021 + x_210 + x_111 + x_010, jxc1), # Perfiles que dan votos al primero de jxc
	Eq(x_201 + x_021 + x_111 + x_001, fr), # Perfiles que dan votos a fr
	# La diferencia de cruces entre lo que esperariamos
	# si todos los que han votado independentista al congreso
	# hubieran puesto tres cruces independentistas,
	# lo atribuimos a los que han puesto una sola cruz
	# por ser FR o por confusion siendo ERC o JxC
	# Ignoramos:
	# - los independentistas que han puesto dos cruces (ni tres, ni una)
	# - los independentistas que se han abstenido en el senado
	# - los no independentistas que han puesto cruz independentista
	#Eq(2*x_001 + 2*x_010 + 2*x_100, sob+congress*3-erc1-erc2-erc3-jxc1-jxc2-jxc3-fr), # Menos de 3 cruces
	# Restricciones para evitar negativos (ver desarrollo abajo)
	# x_001 = A - x_010 - x_100
	Eq(x_001, A - x_010 - x_100),
	# 3*x_010 = - 223076 + B  + A
	# 223076 = erc1 + erc2 - 2*erc3 + fr - 2*jxc1 + jxc2 + jxc3
	Eq(3*x_010, A + B -erc1 -erc2 +2*erc3 -fr +2*jxc1 -jxc2 -jxc3),
	# 3*x_100 = + 155443 + D  + A
	# 155443 = 2*erc1 - erc2 - erc3 - fr - jxc1 - jxc2 + 2*jxc3
	Eq(3*x_100, A + D + 2*erc1 -erc2 -erc3 -fr -jxc1 -jxc2 +2*jxc3),
	# 0 <= A <= 388706; escogemos la mitad, menos aun sale negativo
	Eq(A, 7*(erc1 - 2*erc2 + erc3 + fr + jxc1 - 2*jxc2 + jxc3)/12),
	# 0 <= B <= 223076 + 76489; escogemos 1/6
	Eq(B, 1*(3*erc2 - 3*erc3)/12),
	# 0 <= D <= 366886 - 155443, escogemos 1/6
	Eq(D, 1*(3*jxc2 - 3*jxc3)/12),
]

solution = solve(equations, incognitas)

def value(x):
	try: return int(x)
	except:  return x

for x in solution:
	print(x, "=", value(solution[x].subs(constants)), "=", solution[x] )



"""
Sin aplicar condiciones sobre el signo, del sistema de ecuaciones original, sale:

x_111 = -x_001/3 - x_010/3 - x_100/3 + 388706/3 = erc1/3 - 2*erc2/3 + erc3/3 + fr/3 + jxc1/3 - 2*jxc2/3 + jxc3/3 - x_001/3 - x_010/3 - x_100/3
x_201 = -x_001/3 + 2*x_010/3 - x_100/3 + 223076/3 = erc1/3 + erc2/3 - 2*erc3/3 + fr/3 - 2*jxc1/3 + jxc2/3 + jxc3/3 - x_001/3 + 2*x_010/3 - x_100/3
x_021 = -x_001/3 - x_010/3 + 2*x_100/3 - 155443/3 = -2*erc1/3 + erc2/3 + erc3/3 + fr/3 + jxc1/3 + jxc2/3 - 2*jxc3/3 - x_001/3 - x_010/3 + 2*x_100/3
x_120 = x_001/3 + x_010/3 - 2*x_100/3 + 366886/3 = 2*erc1/3 - erc2/3 - erc3/3 - fr/3 - jxc1/3 + 2*jxc2/3 - jxc3/3 + x_001/3 + x_010/3 - 2*x_100/3
x_210 = x_001/3 - 2*x_010/3 + x_100/3 + 76489/3 = -erc1/3 + 2*erc2/3 - erc3/3 - fr/3 + 2*jxc1/3 - jxc2/3 - jxc3/3 + x_001/3 - 2*x_010/3 + x_100/3

Una suma de votos no puede ser negativa, así que obtenemos las inequaciones:

-x_001/3 - x_010/3 - x_100/3 + 388706/3 >= 0
-x_001/3 + 2*x_010/3 - x_100/3 + 223076/3 >= 0
-x_001/3 - x_010/3 + 2*x_100/3 - 155443/3 >= 0
x_001/3 + x_010/3 - 2*x_100/3 + 366886/3 >= 0
x_001/3 - 2*x_010/3 + x_100/3 + 76489/3 >= 0

Reorganizamos:

-x_001 -   x_010 -   x_100 + 388706 >= 0
-x_001 + 2*x_010 -   x_100 + 223076 >= 0
 x_001 - 2*x_010 +   x_100 +  76489 >= 0
-x_001 -   x_010 + 2*x_100 - 155443 >= 0
 x_001 +   x_010 - 2*x_100 + 366886 >= 0

Reescribimos en funcion de 5 incognitas extrictamente positivas:

-x_001 -   x_010 -   x_100 + 388706 = A ;  A >= 0
-x_001 + 2*x_010 -   x_100 + 223076 = B ;  B >= 0
 x_001 - 2*x_010 +   x_100 +  76489 = C ;  C >= 0
-x_001 -   x_010 + 2*x_100 - 155443 = D ;  D >= 0
 x_001 +   x_010 - 2*x_100 + 366886 = E ;  E >= 0

C y F dependen de B y D y sirven para obtener la cota superior:

>> -x_001 + 2*x_010 -   x_100 + 223076 = B ;  B >= 0
>>  x_001 - 2*x_010 +   x_100 +  76489 = C ;  C >= 0
	B + C = 223076 + 76489
	C = 223076 + 76489 - B >=0   <-  C>=0
::	0 <= B <= 223076 + 76489
>> -x_001 -   x_010 + 2*x_100 - 155443 = D ;  D >= 0
>>  x_001 +   x_010 - 2*x_100 + 366886 = E ;  E >= 0
	D + E = 366886 - 155443
	E = 366886 - 155443 - D >=0   <-  E>=0
::	0 <= D <= 366886 - 155443

Resolvemos el sistema de equaciones:

>>	-x_001 -   x_010 -   x_100 + 388706 = A ;  0 <= A <= 388706
>>	-x_001 + 2*x_010 -   x_100 + 223076 = B ;  0 <= B <= 223076 + 76489
>>	-x_001 -   x_010 + 2*x_100 - 155443 = D ;  0 <= D <= 366886 - 155443

	+x_001 +   x_010 +   x_100 = + 388706 - A
	-x_001 + 2*x_010 -   x_100 = - 223076 + B
	-x_001 -   x_010 + 2*x_100 = + 155443 + D

	3*x_010 = - 223076 + B  + 388706 - A
	3*x_100 = + 155443 + D  + 388706 - A
	x_001 = 388706 -A - x_010 - x_100

		<- (A'=388706-A)

::	x_001 = A - x_010 - x_100
::	3*x_010 = - 223076 + B  + A
::	3*x_100 = + 155443 + D  + A
::	0 <= A <= 388706
::	0 <= B <= 223076 + 76489
::	0 <= D <= 366886 - 155443

Tambien forzamos que x_001, x_010 y x_100 sean positivas

>>	x_100 >= 0
	3*x_100 = + 155443 + D  + A
	No supone más restricciones que las que tenemos,  D>=0, A>=0

>>	x_010 >= 0
	3*x_010 = - 223076 + B  + A >= 0
	A + B >= 223076
	A >= 223076 - B
::	max(0, 223076-A) <= B <= 223076 + 76489

>>  x_001 >=0
	x_001 = A - x_010 - x_100 >= 0
	3*A - 3*x_010 - 3*x_100 >= 0
	3*A >= + 3*x_010 + 3*x_100
	3*A >= + 155443 + D + A - 223076 + B  + A
	A >= + 155443 + D - 223076 + B
::	A >= + 155443 + D - 223076 + B

Expresamos las constantes en términos de las entradas.

388706 = erc1 - 2*erc2 + erc3 + fr + jxc1 - 2*jxc2 + jxc3 = (+1 -2 +1 +1 +1 -2 +1)
223076 = erc1 + erc2 - 2*erc3 + fr - 2*jxc1 + jxc2 + jxc3 = (+1 +1 -2 +1 -2 +1 +1)
155443 = 2*erc1 - erc2 - erc3 - fr - jxc1 - jxc2 + 2*jxc3 = (+2 -1 -1 -1 -1 -1 +2)
366886 = 2*erc1 - erc2 - erc3 - fr - jxc1 + 2*jxc2 - jxc3 = (+2 -1 -1 -1 -1 +2 -1)
76489 = -erc1 + 2*erc2 - erc3 - fr + 2*jxc1 - jxc2 - jxc3 = (-1 +2 -1 -1 +2 -1 -1)

223076 +  76489 = ( 0 +3 -3  0  0  0  0) = 299565 = 3*erc2 - 3*erc3
366886 - 155443 = ( 0  0  0  0  0 +3 -3) = 211443 = 3*jxc2 - 3*jxc3
388706 +  76489 = ( 0  0  0  0 +3 -3  0) = 465195 = 3*jxc1 - 3*jxc2
223076 - 155443 = (-1 +2 -1 +2 -1 +2 -1) = 644636 = -erc1 +2*erc2 -erc3 +2*fr -jxc1 +2*jxc2 -jxc3

"""
