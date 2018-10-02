# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:45:53 2013

@author: Nicolas
"""

from math import sqrt

n=-1
while type(n)!=int or n<=0:  # Condition : un entier n strictement positif
    n=input('n ? ')
    
listeTotale=[]  # Liste contenant les nombres parfaits jusqu'à n

for k in range(1,n+1):  # Boucler tous les entiers de 1 à n

    s=0
    for i in range(1,int(sqrt(k))): # Boucle des nombres parfaits
        if (k%i)==0:
            s=s+i
            if i!=k/i and k/i!=k:
                s=s+k/i

    if s==k:  # Rajouter k à la liste si il est parfait
        listeTotale=listeTotale+[k]
    
print listeTotale