# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:59:35 2013

@author: Nicolas
"""

from random import randint

def nbreDevin():

    difficulte='a'
    
    reponse=raw_input('Voulez-vous choisir le nombre ? ( o / n ) ')
    reponse.lower()
    if reponse=='o':
        nombreC='a'
        while type(nombreC)!=float:
            nombreC=input('Nombre caché ? ')
    else:
        while type(difficulte)!=int:
            difficulte=input(' Quelle est la difficulté choisie ? ( un nombre ) ')
    
        if difficulte<=0:
            nombreC=randint(0,1)
        elif difficulte>0 and difficulte<=5:
            nombreC=randint(0,100*difficulte)
        else:
            nombreC=randint(0,100*difficulte)+float(1)/float(randint(0,100*difficulte))
    
    essais='a'

    while type(essais)!=int:
        essais=input('Combien d\'essais vous vous laissez ? ( -1 = infini ) ')

    nombreP=nombreC+1
    numEssai=-1
    while 1:
        numEssai+=1
        print 'Essai numéro : ',numEssai
        nombreP='a'
        while type(nombreP)!=float:
            nombreP=raw_input('Quel nombre proposez-vous ? ')
            nombreP=float(nombreP)
        
        if nombreP==nombreC:
            print 'Bravo, vous avez gagné ! '
            break
        elif nombreC<nombreP:
            print 'Vous avez proposé un nombre trop grand'
            numEssai+=1
        else:
            print 'Vous avez proposé un nombre trop petit'
            numEssai+=1
        if numEssai>essais+1 and essais>0:
            print 'Vous avez perdu'
            break
    reponse=raw_input('VOulez-vous rejouer ? ( o / n ) ')
    reponse.lower()
    if reponse=='o':
        nbreDevin()

nbreDevin()