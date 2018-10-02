# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:55:43 2013

@author: Nicolas
"""

n=-1
while type(n)!=int or n<0:  # Condition : un entier n strictement positif
    n=input('n ? ')
    
listeTotale=[]  # Liste contenant les nombres parfaits jusqu'à n

for k in range(0,n+1):  # Boucler tous les entiers de 1 à n

    liste=list(str(k))  # Algorithme nombres narcissiques

    s=0
    for i in liste:
        s=s+(int(i)**(len(liste)))

    if s==k:  # Rajoput de k à la liste si il est narcissique
        listeTotale=listeTotale+[k]
    
print listeTotale