# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:46:29 2013

@author: Nicolas
"""

uZero="a"   # u(0)
while type(uZero)!=int:
    uZero=input('Valeur de u(0) : ')
    
uUn="a" #u(1)
while type(uUn)!=int:
    uUn=input('Valeur de u(1) : ')

n=-1    # Rang
while type(n)!=int or n<0 : # Conditions sur n
    n=input('Rentrer n : ')

reponse=raw_input('Voulez-vous afficher tous les termes de la suite ? (o/n) : ')
t=[uZero,uUn]   #Suite sous forme d'une liste

for i in range(2,n+1):
    t.extend([t[i-1]+t[i-2]])
if reponse=="o":    # Affichage de tous les termes de la suite
    print t
else:
    print t[n]  # Affichage du dernier terme de la suite