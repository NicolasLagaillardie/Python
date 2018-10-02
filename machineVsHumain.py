# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:40:25 2013

@author: Nicolas
"""

n=0
reel=1
while reel>0:   # Boucler jusqu'à atteindre la condtion
    try:    # Tant que possible, faire :
        reel=float(1)/float(2**n)
        n+=1
    except: # Sinon : 
        break   # Arrêter la boucle
    
print 'Le plus petit reel possible est : ',reel
print 'Le plus grand n tel que 1/(2^n) > 0 est : ',n
print 'Conclusion : les machines ne font pas de vrais calculs formels'
print 'Remarque : dans la console, à la main, 1/(2**1074) = 5e-324'
print 'Mais 1/(2**107) = 0'