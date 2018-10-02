# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 00:32:34 2015

@author: btapiero
"""

import voyageur_de_commerce_simple
import random
import time

recuit = voyageur_de_commerce_simple.recuit_simulé
stats = voyageur_de_commerce_simple.statistiques

"""3 minutes pour 200 villes"""

n = 20                     # nombre de villes
dmax = 120                  # distance maximale  
k = 0.99                    # loi géométrique de la température
KB = 1.38064852 * 10**(-23) # constante de Boltzmann   
eps = KB/KB                     
N = 100                     # nombre d'itérations

def generate (n, dmax):
    D = [[0]*n]*n
    for i in range (n):
        for j in range (n):
            D [i][j] = random.uniform (0, dmax)
    return D

D = generate (n, dmax)
print (D)
print (voyageur_de_commerce_simple.recuit_simulé (D, eps, k, N))
a = time.time()
stats (D, eps, k, N)
print (time.time() - a)