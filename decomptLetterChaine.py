# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:02:35 2013

@author: Nicolas
"""

# Entre une chaine de caractère et renvoie le nombre de fois que chacun
# des caractères apparaît dans l'entrée

def frequence(chaine='azertya'):
    """ chaine -> dictionnaire ( caractère : valeur ) """
    from copy import deepcopy
    tmp=deepcopy(chaine)
    dico={}
    for i in tmp:
        tmp2=0
        for k in tmp:
            if k==i:
                tmp2=tmp2+1
                del k
        dico[i]=tmp2
        del i
    return dico