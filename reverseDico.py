# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:02:35 2013

@author: Nicolas
"""

# Fonction permettant d'inverser les clés et les valeurs d'un dictionnaire

def inverser(dico):
    """ Le dictionnaire d'entré ne doit avoir aucune valeur commune à deux clés
    distinctes """
    tmp={}  # Programme non optimisé car création d'un dictionnaire tier
    for i in dico:
        tmp[dico[i]]=i  # Les valeurs de l'entrée sont les clés de la sortie
    return tmp