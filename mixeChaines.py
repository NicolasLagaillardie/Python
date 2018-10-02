# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:14:43 2013

@author: Nicolas
"""

# Entre deux chaines et renvoie un mix des deux chaines dépendant de
# la chaîne le plus petite 

def mixer(chaine1='02468',chaine2='13579'):
    """ Chaine1 , Chaine2 """
    chaine3=''
    for i in range(0,min(len(chaine1),len(chaine2))-1):
        chaine3=chaine3+chaine1[i]+chaine2[i]
    return chaine3