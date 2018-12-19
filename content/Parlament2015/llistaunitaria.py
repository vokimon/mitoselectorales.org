#!/usr/bin/env python3

"""
Simulacion de probabilidades
"""

import numpy as np

def add(dist1, dist2):
    "Adds two distributions"
    result = np.zeros(len(dist1)+len(dist2))*1.
    for i, probability1 in enumerate(dist1):
        for j, probability2 in enumerate(dist2):
            result[i+j] += probability1*probability2
    return result

dist1 = np.ones(100,np.float32)/100.
dist2 = add(dist1, dist1)
dist3 = add(dist2, dist1)
dist4 = add(dist3, dist1)
dist5 = add(dist4, dist1)

dist1.resize(len(dist5))
dist2.resize(len(dist5))
dist3.resize(len(dist5))
dist4.resize(len(dist5))


import matplotlib.pyplot as plt
plt.plot(dist1,'b')
plt.plot(dist2,'b--')
plt.plot(dist3, 'b:')
plt.plot(dist4,'b')
plt.plot(dist5,'b--')
plt.legend([1, 2, 3, 4, 5], 'center right',
	title="Candidatures\nunificades")
plt.xlabel("Vots (percentatge del preu de l'escò)")
plt.ylabel('Probabilitat')
plt.title('Probabilitat a una circumscripció de treure escons per suma de restos')
for i in range(6) :
	plt.text(50+i*100, .012, '{}\nESCONS'.format(i), horizontalalignment='center')
for i in range(0,5,2):
    plt.axvspan(i*100, i*100+100, facecolor='0.1', alpha=0.1)
plt.axis([0, 600, 0, 0.015])
plt.grid(True)
plt.savefig('llistaunitaria-sumarestos.png')
plt.show()


pools = np.random.random_integers(0,1000000, (20,1000000))
totals = pools.sum(0)
scons = 30./totals * pools
sobrants = scons%1
print(sobrants.sum(0))

plt.plot(np.histogram(sobrants.sum(0), bins=np.arange(20))[0])
plt.show()








