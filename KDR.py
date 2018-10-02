# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:05:53 2016

@author: Nicolas
"""

from random import randint

def choix(total,n=3):
    fichier=open('KDR.txt','r')
    liste=fichier.read()
    liste=liste.split('\n')

    L = []
    for i in range(len(liste)):
        try:
            L.append(int(i))
        except:
            1

    restants = []
    for i in range(total):
        if i not in L :
            restants.append(i)
            
    L = []
    k=0
    
    fichier.close()
    fichier=open('KDR.txt','a')
    
    while k < n :
        a = randint(1,len(restants))
        if a not in L :
            print 'KDR numéro : '+str(restants[a])
            fichier.write(str(restants[a])+'\n')
            k += 1
        
    fichier.close()