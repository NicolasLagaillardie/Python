#Algorithme de Prim non optimisé : création de nombreuses variables et listes pouvant sûrement être remplacées/éludées
#rajouter un nombre != 0 pour éviter d'afficher toutes les boucles
# -*- coding: cp1252 -*-
# -*- coding: latin-1 -*-

print 'Version 1.0, par Lockas et Esmar, 08 Mai 2013'
print 'Optimisé pour Python 2.7'
print 'Par défaut, le graphe est : [[1,8,2,7,3,1,4,0],[0,8,2,15,3,4,4,5],[0,7,1,15,3,2,4,6],[0,1,1,4,2,2,4,2],[0,0,1,5,2,6,3,2]]'
print 'Attention de bien mettre TOUS les liens entre les sommets'
print 'Attention d\'utiliser un graphe connexe'

from Tkinter import *
from math import *
	
def Prim(graphe=[[1,8,2,7,3,1,4,0],[0,8,2,15,3,4,4,5],[0,7,1,15,3,2,4,6],[0,1,1,4,2,2,4,2],[0,0,1,5,2,6,3,2]],pedago=0):
	"""Prim(graphe,affichage pedagogique) avec graphe sous la forme [[voisin1,poids1,...],[],...[]]"""

	#Si le graphe correspond à  un espace vide, à  un seul point ou n'est pas sous la forme d'un tableau
	if type(graphe)!=type([]) or len(graphe)==0:
		print 'Le graphe en question n\'en est pas un !'
		return
	if len(graphe)==1:
		print 'Le seul arbre courant dans le cas présent est le sommet donné !'
		return
	vrai=0
	for k in range(0,len(graphe)):
		for i in range(0,len(graphe[k])):
			if len(graphe[k])!=0:
				vrai=1
	if vrai==0:
		print 'Le graphe en question n\'en est pas un !'
		return
	
	#Début de l'algorithme à  proprement parler
	i=0	#Sommet de départ
	tabpoids=[]
	sommets=[0]
	compteur=1
	if pedago==0:
		print 'Graphe utilisé : ',graphe
		print 'Départ du sommet n°0'
		print ''
	while len(sommets)<len(graphe)*2-1:	#Boucle globale : permet de construire l'arbre avec tous les sommets du graphe
		#Compteur de boucle
		if pedago==0:
			print 'Boucle n° : ',compteur
		
		graphint=graphe[i]
		graphintsave=[]		#graphintsave permet de garder intact le graphe initial
		for k in range(0,len(graphint)):
			graphintsave.extend([graphint[k]])
		graphintsave=(graphintsave,)
		#Boucles premettant d'éviter de choisir parmis des sommets déjà  atteints
		for k in range(0,len(sommets)):
			vrai=0
			j=0
			while vrai==0:
				if sommets[k]==graphint[j]:
					del(graphint[j])
					del(graphint[j])
					j=j-2
				j=j+2
				if j>=len(graphint):
					vrai=1
		del(graphe[i])
		graphe.insert(i,graphintsave[0])
		if pedago==0:
			print 'Sommet de départ : ',i
		
		#Boucles de recherche de l'arête avec le poids le plus faible ainsi que des sommets qu'elle atteint
		poids=max(graphint)
		for k in range(1,len(graphint),2):
			if graphint[k]<poids:
				poids=graphint[k]
		if pedago==0:
			print 'poids minimal : ',poids
		for k in range(-1,len(graphint),2):
			if graphint[k]==poids:
				sommet=k-1
		if pedago==0:
			print 'sommet correspondant : ',graphint[sommet]
					
		#Rajout du poids et du sommet
		tabpoids.extend([graphint[sommet+1]])
		sommets.extend([graphint[sommet]])
		
		#Boucles permettant de trouver le prochain sommet dont l'une des arêtes a le poids le plus faible dans le graphe : arbre + sommets atteints dans le graphe final
		graphint2=graphint3=[]
		for k in range(0,len(sommets)):
			graphint2.extend(['*',sommets[k]])
			graphint3=graphe[sommets[k]]
			for j in range(0,len(graphint3)):
				graphint2.extend([graphint3[j]])
		for k in range(0,len(sommets)):
			vrai=0
			j=0
			while vrai==0:
				if sommets[k]==graphint2[j]:
					del(graphint2[j])
					del(graphint2[j])
					j=j-2
				j=j+2
				if j>=len(graphint2):
					vrai=1
		poids=max(graphint2)
		for k in range(1,len(graphint2),2):
			if graphint2[k-1]=='*':
				sommetchoisi=graphint2[k]
			if graphint2[k]<poids and graphint2[k-1]!='*':
				poids=graphint2[k]
				i=sommetchoisi
		compteur=compteur+1
		sommets.extend([i])
		
		#Affichage des paramêtres importants len(sommets)<len(graphe)*2-1
		if pedago==0:
			if len(sommets)<len(graphe)*2-1:
				print 'Prochain sommet de départ : ',i
			print 'tableau des poids : ',tabpoids
			print 'tableau des sommets : ',sommets
			print ''

	#Evite d'afficher un graphe cyclique au lieu d'un arbre
	del(sommets[len(sommets)-1])
	#Affichage de l'arbre sous la forme : sommet -> poids -> sommet
	print 'Le chemin final est : 0',
	for i in range(0,len(tabpoids)):
		print '{',tabpoids[i],'}',sommets[2*i+1],' ->',
		try:
			print sommets[2*i+2],
		except:
			print 'Fin'
	
	#Interface graphique du graphe
	mastergraphe = Tk()
	cv = Canvas(mastergraphe, width=800, height=600)
	cv.pack()
	Button(mastergraphe, text="Quitter", command = mastergraphe.destroy).pack()
	
	#Listes des coordonnées
	#Peuvent être calculées directement dans la boucle mais moins lisible
	listecoordonnees=[]
	for i in range(0,len(graphe)):
		listecoordonnees.extend([int(250*(cos(2*float(pi)*i/(len(graphe)))))+400,int(250*(sin(2*float(pi)*i/(len(graphe)))))+300])
	listecoordonneesS=[]
	for i in range(0,len(graphe)):
		listecoordonneesS.extend([int(260*(cos(2*float(pi)*i/(len(graphe)))))+400,int(260*(sin(2*float(pi)*i/(len(graphe)))))+300])
	
	#Création du graphe
	for sommetdep in range(0,len(graphe)):
		graphint=graphe[sommetdep]
		for sommetarr in range(0,len(graphint),2):
			cv.create_line((listecoordonnees[2*sommetdep],listecoordonnees[2*sommetdep+1]),(listecoordonnees[2*graphint[sommetarr]],listecoordonnees[2*graphint[sommetarr]+1]))		#Création et placement du lien
			
			rayon=15+sqrt(pow(float(int((listecoordonnees[2*sommetdep]+listecoordonnees[2*graphint[sommetarr]])/2)-400),2)+pow(float(int((listecoordonnees[2*sommetdep+1]+listecoordonnees[2*graphint[sommetarr]+1])/2)-300),2))	#Rayon, pour le placement du poids de l'arête
			
			#Angle, pour le placement du poids de l'arête
			angleC=cos(2*float(pi)*((abs(graphint[sommetarr]-sommetdep)/float(2))+(min((sommetdep,graphint[sommetarr]))))/(len(graphe)))
			angleS=sin(2*float(pi)*((abs(graphint[sommetarr]-sommetdep)/float(2))+(min((sommetdep,graphint[sommetarr]))))/(len(graphe)))
			"""print sommets[sommetdep],sommets[sommetarr],abs(400-int((rayon-3)*angleC+400)),abs(int(abs(listecoordonnees[2*sommets[sommetarr]]+listecoordonnees[2*sommets[sommetdep]])/float(2))),int((rayon-3)*angleC+400),abs(int((listecoordonnees[2*sommets[sommetdep]+1]+listecoordonnees[2*sommets[sommetarr]+1])/float(2))),int((rayon-3)*angleS+300)"""
			if abs(int(abs(listecoordonnees[2*graphint[sommetarr]]+listecoordonnees[2*sommetdep])/float(2))-int((rayon-3)*angleC+400))>int(abs(15)):#or abs(400-int((rayon-3)*angleC+400))<9:
				angleS=-angleS
				angleC=-angleC
			
			#Coordonnées finales, pour le placement du poids de l'arête
			#Blocs Rayon, Angle et Coordonnées peuvent être réunnis en un seul bloc, moins lisible mais plus léger pour des gros graphes
			coordonneesX=int((rayon-5)*angleC+400)
			coordonneesY=int((rayon-5)*angleS+300)
			
			cv.create_text(listecoordonneesS[2*sommetdep],listecoordonneesS[2*sommetdep+1],text=str(sommetdep))	#Création et placement du nom des sommets
			cv.create_text(coordonneesX,coordonneesY,text=graphint[sommetarr+1])	#Création et placement des poids
			cv.create_text(60,570,text='Graphe initial utilisé')
	
	#Interface graphique de l'arbre
	masterarbre = Toplevel()	#Toplevel permet d'afficher deux fenêtres simultanément
	cv = Canvas(masterarbre, width=800, height=600)
	cv.pack()
	Button(masterarbre, text="Quitter", command = masterarbre.destroy).pack()
	
	#Création du graphe
	for sommetdep in range(0,len(sommets),2):
		for sommetarr in range(1,len(sommets),2):
			if sommets[sommetdep]==sommets[sommetarr-1]:
				cv.create_line((listecoordonnees[2*sommets[sommetdep]],listecoordonnees[2*sommets[sommetdep]+1]),(listecoordonnees[2*sommets[sommetarr]],listecoordonnees[2*sommets[sommetarr]+1]))		#Création et placement du lien
			
				rayon=15+sqrt(pow(float(int((listecoordonnees[2*sommets[sommetdep]]+listecoordonnees[2*sommets[sommetarr]])/2)-400),2)+pow(float(int((listecoordonnees[2*sommets[sommetdep]+1]+listecoordonnees[2*sommets[sommetarr]+1])/2)-300),2))	#Rayon, pour le placement du poids de l'arête
			
				#Angle, pour le placement du poids de l'arête
				angleC=cos(2*float(pi)*((abs(sommets[sommetarr]-sommets[sommetdep])/float(2))+(min((sommets[sommetdep],sommets[sommetarr]))))/(len(graphe)))
				angleS=sin(2*float(pi)*((abs(sommets[sommetarr]-sommets[sommetdep])/float(2))+(min((sommets[sommetdep],sommets[sommetarr]))))/(len(graphe)))
				"""print sommets[sommetdep],sommets[sommetarr],abs(int(abs(listecoordonnees[2*sommets[sommetarr]]+listecoordonnees[2*sommets[sommetdep]])/float(2))),int((rayon-3)*angleC+400),abs(int((listecoordonnees[2*sommets[sommetdep]+1]+listecoordonnees[2*sommets[sommetarr]+1])/float(2))),int((rayon-3)*angleS+300)"""
				if abs(int(abs(listecoordonnees[2*sommets[sommetarr]]+listecoordonnees[2*sommets[sommetdep]])/float(2))-int((rayon-3)*angleC+400))>15:
					angleS=-angleS
					angleC=-angleC
				if abs(int((listecoordonnees[2*sommets[sommetdep]+1]+listecoordonnees[2*sommets[sommetarr]+1])/float(2))-int((rayon-3)*angleS+300))>13:
					angleS=-angleS
					angleC=-angleC
			
				#Coordonnées finales, pour le placement du poids de l'arête
				#Blocs Rayon, Angle et Coordonnées peuvent être réunnis en un seul bloc, moins lisible mais plus léger pour des gros graphes
				coordonneesX=int((rayon-5)*angleC+400)
				coordonneesY=int((rayon-5)*angleS+300)
			
				cv.create_text(listecoordonneesS[2*sommets[sommetdep]],listecoordonneesS[2*sommets[sommetdep]+1],text=str(sommets[sommetdep]))	#Création et placement du nom des sommets
				cv.create_text(listecoordonneesS[2*sommets[sommetarr]],listecoordonneesS[2*sommets[sommetarr]+1],text=str(sommets[sommetarr]))	#Création et placement du nom des sommets
				cv.create_text(coordonneesX,coordonneesY,text=tabpoids[int(float(sommetarr-1)/float(2))])	#Création et placement des poids
				cv.create_text(60,570,text='Arbre')
	mainloop()
