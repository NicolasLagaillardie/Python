# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:22:47 2013

@author: Nicolas
"""

A=-1
while type(A)!=float or A<0:  # Conditions : A reel strictement positif
    A=input('A ? ')
    try:    # Si A est autre chose qu'un nombre, alors faire :
        A=float(A)  # Permet d'obtenir un reel à partir d'un nombre quelconque
    except: # Sinon
        print ''

print ''

s=0
n=0
while s<=A: # Boucler jusqu'à dépasser la condition
    n=n+1
    s=s+float(1)/float(n)
        
print 'Au rang ',n,' , Un vaut ',s,' qui est plus grand que ',int(A)