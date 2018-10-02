# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:34:37 2013

@author: Nicolas
"""

import os   # Importe une librairie de commandes avancées

A=-1
while type(A)!=int or A<=0: # Conditions : A entier strictement positif
    A=input('A ? ')

if A==1:    # Si A est trop petit
    print ' 1 ! = ',A
    os.system("pause")  # Met le système en pause

s=1
n=0
while s<=A: # Boucler jusqu'à atteindre la condition stricte
    n=n+1
    s=1
    for i in range(1,n+1):	# Calcul de la factorielle
        s=s*i
        
print 'On a bien ',n,'! = ',s,' > ',A,' et ',n-1,'! = ',s/n,' < ou = ',A