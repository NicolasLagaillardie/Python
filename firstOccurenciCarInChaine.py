# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:21:44 2013

@author: Nicolas
"""
 
# pos renvoie la première occurence de car dans chaine

def pos(chaine='azerty',car='e'):
    if car not in chaine:
        return 'Le carcatère ',car,' n\'est pas dans la chaine ',chaine
    print 'Le caractère ',car,' est situé au ',chaine.find(car),'-ième indice'