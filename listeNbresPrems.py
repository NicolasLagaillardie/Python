# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:04:27 2013

@author: Nicolas
"""

def listeNbPre(n):
    from math import sqrt
    fichier=open('listeNbresPremiers.txt','a')

    for i in range(2,n+1):
        j=0
        for k in range(2,int(sqrt(i))+1):
            if i%k==0:
                j=1
                break
            if j==0:
                fichier.write(str(i)+'\n')
                
    fichier.close()