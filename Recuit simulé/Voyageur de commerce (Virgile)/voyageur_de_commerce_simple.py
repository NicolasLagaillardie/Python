# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 00:30:26 2015

@author: btapiero
"""

import random
import math
import matplotlib.pyplot as plt

def melange (l):
    L = []
    p = []
    for elt in l: 
        L += [elt]
    for i in range (len (l)):
        k = random.randint (0, len (l) -1)
        while k in p:
            k = random.randint (0, len (l) -1)            
        p += [k]
    for i in range (len (l)):
        l [i] = L [p [i]]
        
def derangement (c):
    melange (c)
    return c
    
def distance (D, c):
    d = 0
    for i in range (len (c)-1):
        d += D [c[i]][c[i+1]]
    return d
    
def ensemble (n):
    L = []
    for i in range (n):
        L.append (i)
    return L
    
def loi_tempétare (K, T):
    return K * T

def recuit_simulé (D, eps, k, N):
    T = 1
    chemin_test = derangement (ensemble (len (D [0])))
    distance_test = distance (D, chemin_test)
    n = 0
    while n < N:
        T = loi_tempétare (k, T)
        Palier = math.exp (eps/T)
        iteration = 0
        while iteration < Palier:
            chemin_test_temporaire = derangement (chemin_test)
            distance_test_temporaire = distance (D, chemin_test_temporaire)
            if distance_test_temporaire < distance_test:
                chemin_test = chemin_test_temporaire
                distance_test = distance_test_temporaire
            else:
                Proba = math.exp ((distance_test - distance_test_temporaire)/T)
                if random.uniform (0, 1) < Proba:
                    chemin_test = chemin_test_temporaire
                    distance_test = distance_test_temporaire
            iteration += 1
        n += 1
    #print (chemin_test)
    return distance_test
    
def statistiques (D, eps, k, N):
    X = []
    Y = []
    for i in range (N+1):
        X.append (i)
        Y.append (recuit_simulé (D, eps, k, 100))
    moyenne = 0
    for elt in Y:
        moyenne += elt
    moyenne = moyenne/(len(X))
    m = min (Y)
    M = max (Y)
    plt.scatter (X, Y)
    plt.plot (X, [moyenne for x in X])
    plt.plot (X, [m for x in X])
    plt.plot (X, [M for x in X])
    plt.show ()