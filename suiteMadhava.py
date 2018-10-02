# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:13:07 2013

@author: Nicolas
"""

from math import pi,sqrt

e=-1
while type(e)!=float or e<0:    # Conditions : e entier strictemnt positif
    e=input('e ? ')
    print ''

n=0
s=0
while abs(s-pi)>=e: # Boucler jusqu'à dépasser la condition
    n=n+1
    s=0
    for i in range(0,n+1):  # Calcul de la suite
        s=s+sqrt(12)*(float((-3)**(-i))/(float(2*i+1)))
        
#Affichage des résultats

print 'Xn = ',s,' | Xn - pi | = ',abs(s-pi),' n = ',n