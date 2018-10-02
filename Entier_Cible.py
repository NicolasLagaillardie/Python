# -*- coding: cp1252 -*-
#Entier Cible


def foundit(I,n):       #Cherche la liste la plus courte
	if I[len(I)-1]==n:
		return I
	k=len(I)-1
	while k>=0:
		if I[k]+I[len(I)-1]<=n:
			return foundit(I+[I[len(I)-1]+I[k]],n)
		k=k-1
		
def toutTrouver(I,n):   #Cherche toutes les listes possibles
	Inter=[]
	ToFind=foundit(I,n)
	for k in range(1,n):
		nbre=foundit(I,k)
		if len(nbre)<=len(ToFind)-1:
			for j in nbre:
				if j+nbre[len(nbre)-1]==n:
					Inter.extend([nbre+[n]])
	return Inter

def listeFinale(n):     #Fonction laucher
	"""n, l'entier qu'on recherche"""
	I=[1]
	for k in toutTrouver(I,n):
		print k
