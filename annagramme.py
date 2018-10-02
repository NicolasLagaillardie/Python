# -*- coding: cp1252 -*-
#Annagramme

def facto(nombre):
	while type(nombre)!=type(5):
		print 'Veuillez donner un nombre valide'
		nombre=raw_input()
		nombre=int(nombre)
	for i in range(1,nombre):
		nombre=nombre*i
	return nombre

def annagramme(nom):
	while type(nom)!=type(''):
		print 'Veuillez donner une chaîne de caractère valide'
		nom=raw_input()
	from random import shuffle
	nom=nom.lower()
	nom=list(nom)
	lim=facto(len(nom))
	table=[]
	if lim>100:
		lim=100
	for i in range(0,lim):
		shuffle(nom)
		chaine=''
		for k in range(0,len(nom)):
			if k==0 or nom[k-1]==' ':
				nom=nom.upper()
			else:
				nom=nom.lower()
			chaine=chaine+nom[k]
		if chaine not in table:
			print chaine
			table.extend([chaine])