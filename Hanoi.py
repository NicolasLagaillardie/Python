# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 09:03:47 2013

@author: Nicolas
"""

#Programme résolvant le jeux des tours de Hanoi

def Hanoi(NbAnneaux,TourOrigine,TourDestination,TourIntermediaire):
	if NbAnneaux==1:
		print '>>> Deplacement de la tour %s '% TourOrigine,'vers la tour %d ' %TourDestination
	else:
		Hanoi(NbAnneaux-1,TourOrigine,TourIntermediaire,TourDestination)
		Hanoi(1,TourOrigine,TourDestination,0)
		Hanoi(NbAnneaux-1,TourIntermediaire,TourDestination,TourOrigine)
		
NbAnneaux=input('Rentrez le nombre d\'anneaux : ')

Hanoi(NbAnneaux,1,2,3)