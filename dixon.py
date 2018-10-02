# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:58:51 2013

@author: Nicolas
"""

# Algorithme Dixon

from listeNbresPrems import listeNbPre
from random import randint

def Dixon(n):
    
    from math import log10,sqrt

    N=sqrt(2*(log10(n)*log10(log10(n))))
    
    listeNbPre(int(N)+1)
    
    for i in range(0,int(N)+1):
        randint()