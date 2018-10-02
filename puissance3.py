#Codage du jeu cercle/croix
#cahier des charges :
#1 : un ou deux joueurs, IA à rajouter
#2 : jeu au tour par tour, chaque équipe ayant sa couleur de jetons
#3 : nombre de jetons ? illimité ? si non, combien ?  -> taille de la grille ?
#5 : aligner 3 jetons ( ou plus ? )de même couleur, soit horizontalement, soit verticalement, soit en diagonale
#6 : quand arrêter la partie ?
#7 : le jeu se passe dans une grille matérialisable par une matrice

#Pour des raisons de simplicités, ce sera un ronds/croix sur une grille de 3 x 3.

# -*- coding: cp1252 -*-
# -*- coding: latin-1 -*-

from Tkinter import *
from random import randint

def alignes(mat_croix,mat_ronds):	#Permet de détecter l'alignement de plusieurs jetons de même symbole
	#A démarrer qu'à partir du troisième tour compris pour optimiser
	
	#Pour les croix
	for k in mat_croix:
		mat_croix[k]=tmp
		if tmp[0]==6:
			if tmp[1]==1:
				print 'le joueur croix a gagné le long de la colonne n°',tmp[2]
				return 1
			if tmp[1]==2:
				print 'le joueur croix a gagné le long de la ligne n°',tmp[2]
				return 1
			else:
				print 'le joueur croix a gagné le long de la diagonale n°',tmp[2]
				return 1
				
	#pour les ronds
	for k in mat_ronds:
		mat_ronds[k]=tmp
		if tmp[0]==-3
			if tmp[1]==1:
				print 'le joueur ronds a gagné le long de la colonne n°',tmp[2]
				return 1
			if tmp[1]==2:
				print 'le joueur ronds a gagné le long de la ligne n°',tmp[2]
				return 1
			else:
				print 'le joueur ronds a gagné le long de la diagonale n°',tmp[2]
				return 1
	return 0

def data_Saved(graphe_Position):	#Détermine, place et sauvegarde la position des jetons
	save=[]
	compteur=0
	for i in range (0,3):
		for k in range (0,3):
			save=save+[(i,k,graphe_Position[compteur])]
			compteur+=1
	print 'La matrice ',save,' a bien été sauvegardée'
	return save
			
def parametres():	#Choix des paramètres : nombre de joueurs et choix des symboles
	verif=-1
	print 'Combien y a-t-il de joueur(s) humain(s) qui joue(nt) ( 0 / 1 / 2 ) ?'
	nbreJoueur=-1
	while nbreJoueur==-1:
		nbreJoueur=raw_input()
		try:
			nbreJoueur=int(nbreJoueur)
		except:
			nbreJoueur=-1
		if nbreJoueur<0 or nbreJoueur>2:
			print 'Veuillez donner un nombre de joueurs valide'
			nbreJoueur=-1
	print ''
	
	if nbreJoueur==1:
		print 'Voulez-vous être le premier joueur ou le second joueur ? ( 1 ou 2 )'
		print 'Si vous avez choisi 0 joueurs, entrez n\'importe quel entier'
		verif=0
		while verif==0:
			verif=raw_input()
			try:
				verif=int(verif)
			except:
				verif=-1
			if verif==1:
				print 'Vous êtes le premier joueur'
			elif verif==2:
				print 'Vous êtes le second joueur'
			else:
				print 'Veuillez sélectionner un numéro de joueur valide'
				verif=0
		print ''
		print 'Quelle difficulté voulez-vous ? A partir de 0'
		diff=-1
		while diff<0:
			diff=raw_input()
			try:
				diff=int(diff)
			except:
				diff=-1
			if diff>=0:
				print 'Vous avez choisi une difficulté de : ',diff
			else:
				print 'Veuillez sélectionner une difficulté valide'
				diff=-1
		print ''
	
	if nbreJoueur!=0:	#Non utile : on peut commencer par un symbole imposé
		print 'Voulez-vous être les ronds ou les croix ( R / C )'
		choix_Sym_1=0
		while choix_Sym_1==0:
			choix_Sym_1=raw_input()
			choix_Sym_1.upper()
			if choix_Sym_1=='R':
				print 'Vous avez choisi le symbole Ronds'
				choix_Sym_2='C'
			elif choix_Sym_1=='C':
				print 'Vous avez choisi le symbole Croix'
				choix_Sym_2='R'
			else:
				print 'Veuillez sélectionner un symbole valide'
				choix_Sym_1=0
		print ''
	
	return [nbreJoueur,diff,choix_Sym_1,choix_Sym_2,verif]
	
def liste_Dsipo(listeCoupsJoues):	#Donne la liste des coups jouables
	tmp=[[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]	#tmp peut être construit par un algorithme, pour des grilles de taille variable
	i=0
	compteur=0
	while i==0:
		if tmp[compteur] in listeCoupsJoues:
			del tmp[compteur]
			compteur=compteur-1
		compteur=compteur+1
		if compteur==len(tmp):
			i=1
	return tmp
				
def IA(grille,diff=0):
	coupJoue=liste_Dispo(grille)
	if diif<=0:
		return coupJoue[randint(1,len(coupJoue)-1]
	j=0
	
				
def puissance3():	#Début de la partie
	donnees=parametres()
	mat_croix=[]
	mat_ronds=[]
	match=0
	listeCoupsJoues=[]
	if donnees[0]==1:
		if donnees[4]==1:
			joueurSuivant=2
			joueurActuel=1
		elif donnees[4]==2:
			print 'Joueur actuel : 1'
			joueurActuel=2
			joueurSuivant=1
			print ''
	
	while match==0:
		print 'Joueur actuel : ',joueurActuel
		
		
		
		match=alignes(grille[0],grille[1])
	print 'Le joueur ',joueurActuel,' a gagné'	
	print ''
	print 'Voulez vous recommencer une autre partie ? y or n'
	reponse=raw_input()
	reponse.lower()
	if reponse=='y':
		puissance3()