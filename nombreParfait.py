# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:46:31 2013

@author: Nicolas
"""

from math import sqrt

n=-1
while type(n)!=int or n<=0:  # Un entier n strictent positif
    n=input('n ? ')

s=0
for i in range(1,int(sqrt(n))): # Cherhcer jusqu'à la racine carrée réduit 
    if (n%i)==0:    # les calculs
        s=s+i
        if i!=n/i and n/i!=n:   # Le bloc permet de récupérer les diviseurs de 
            s=s+n/i # n strictements supérieurs à racine carrée de n
    print s
            
# Affichage du résultat
            
if int(s)==int(n):
    print n,' est un nombre parfait'
else:
    print n,' n\'est pas un nombre parfait'