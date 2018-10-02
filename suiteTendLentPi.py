# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:16:23 2013

@author: Nicolas
"""

from math import pi

e=-1
while type(e)!=float or e<0:    # Conditions : e antier strictement positif
    e=input('e ? ')
    print ''

n=0
s=0
while abs(s-pi)>=e: # Boucler jusqu'à dépasser la condtition
    n=n+1
    s=0
    for i in range(0,n+1):  # Calcul de la suite
        s=s+4*(float((-1)**i))/(float(2*i+1))
        
# AFfichage des résultats
        
print 'Wn = ',s,' |Wn-pi| = ',abs(s-pi),' n = ',n