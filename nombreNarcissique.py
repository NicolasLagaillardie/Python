# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:52:19 2013

@author: Nicolas
"""

n=-1
while type(n)!=int or n<=0:  # Condition : un entier n strictement positif
    n=input('n ? ')

liste=list(str(n))  # Permet de séparer tous les chiffres de n dans une liste

s=0
for i in liste: # Boucler pour la somme
    s=s+(int(i)**(len(liste)))

# Affichage des résultats

if s==n:
    print n,' est un nombre narcissique'
else:
    print n,' n\'est pas un nombre narcissique'