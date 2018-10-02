# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:19:08 2013

@author: Nicolas
"""

# Entre une chaine et un caractère et renvoie
# le nombre de fois que le caractère apparaît dans la chaîne

def nb(chaine='azertya',car='a'):
    if car not in chaine:
        return 'Le carcatère ',car,' n\'est pas dans la chaine ',chaine
    else:
        k=0
        for i in chaine:
            if i==car:
                k=k+1
                
        print 'Il y a ',k,' occurence(s) de ',car,' dans la chaine ',chaine