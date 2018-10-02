# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:02:35 2013

@author: Nicolas
"""

# Dans une liste de nombres entiers entre 0 et 100, renvoie l'intervalle
# dans lequel chacun est compris

def compter(L):
    """ Bornes entre 0 et 100 """
    for k in range(0,10):
        tmp=0
        for i in L:
            if i>=10*k and i<10-(k+1):
                tmp=tmp+1
        print 'Il y a ',tmp,' éléments de ',L,
        print ' qui sont dans l\'intervalle [',10*k,',',10*(k+1),'['