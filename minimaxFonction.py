# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
C:\Users\Nicolas\.spyder2\.temp.py
"""

def minimax(*args):
    try:    # Essayer
        mini,maxi=args[0],args[0]
    except: # Sinon
        return 'les arguments ne sont pas valides ou la liste entrée est vide'
    
    for i in args:
        if i>maxi:  # Maxi est le plus grand élément
            maxi=i
        elif i<mini:    # Maxi est le plus petit élément
            mini=i
    print 'Le minimum des arguments est : ',mini,'\n Le maximum des arguments est : ',maxi
    return maxi,mini    # Si la fonction est réutilisée