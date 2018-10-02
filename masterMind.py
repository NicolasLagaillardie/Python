#MasterMind
# -*- coding: cp1252 -*-
# -*- coding: latin-1 -*-

from random import randint
print 'Ce programme marche avec Python 2.7'

def IA(diff):
	confCachee=[]
	if diff<=0:
		for i in range(0,4):
			confCachee=confCachee+[randint(0,1)]
	else:
		for i in range(0,4):
			confCachee=confCachee+[randint(0,diff)]
			
	return confCachee

def partie(diff):

	confCachee=IA(diff)
	
	nbEssais=1
	finPartie=False
	gagne=False

	while not finPartie:
	
		print 'Essai n°',nbEssais
		print 'Veuillez s�parer les nombres par une virgule'
		print ''
		
		confProposee=raw_input()
		confProposee=str(confProposee)
		confProposee=confProposee.split(",")
		while len(confProposee)!=4:
			print 'Veuillez donner une combinaison de format correct'
			confProposee=raw_input()
			confProposee=str(confProposee)
			confProposee=confProposee.split(",")
			print ''
		for i in confProposee:
			i=int(i)
		
		numBienPlaces=0
		numMalPlaces=0
		for i in range(0,4):
			if confProposee[i]==str(confCachee[i]):
				numBienPlaces=numBienPlaces+1
		for i in confProposee:
			if int(i) in confCachee:
				numMalPlaces=numMalPlaces+1
		numMalPlaces=numMalPlaces-numBienPlaces
		print 'Nombre de pions bien placés : ',numBienPlaces
		print 'Nombre de pions mal placés : ',numMalPlaces
		if numBienPlaces==4:
			gagne=True
		
		if gagne==True or nbEssais==10:
			finPartie=True
		else:
			nbEssais=nbEssais+1
		print ''
			
	if gagne:
		print 'Gagné'
	else:
		print 'Perdu'
		
	print ''
	print 'Voulez vous recommencer une autre partie ? y or n'
	reponse=raw_input()
	reponse.lower()
	if reponse=='y':
		parametres()
		
def parametres():
		
	diff='a'
	print 'Quelle difficulté voulez-vous ? ( un nombre entier )'
	while type(diff)!=int:
		print 'Veuillez donner une difficulté valide'
		diff=input()
		print ''
	partie(diff)

parametres()
