#Associer ce programme au fichier texte (liste.txt) constitue de deux colonnes : une avec le prenom et le nom des eleves. une autre contenant le nombre de devoir non surveille rendu
#Faire à l'attention à eviter la presence d'un fichier copie.txt dans le dossier de travail
#Python 2.7

# -*- coding: cp1252 -*-
# -*- coding: latin-1 -*-

from random import randint
import os

fichier=open('liste.txt','r')
copie=open('copie.txt','w')
	
liste=fichier.read()
liste=liste.split('\n')

tmp1=[]
for i in liste:
        i=i.split(' ')
        tmp1=tmp1+i

tmp2=[]
b=5
while b>0:
	try:
		tmp2=tmp2+[[tmp1[b]+' '+tmp1[b+1],int(tmp1[b+2])]]
		b=b+3
	except:
		b=-1
liste=tmp2
		
listeElevesChoisis=[]
listeNumeros=[]
tmp3=[]

for i in range(12):
	b=0
	while b>=0:
		numero=randint(1,len(liste)-1)
		couple=liste[numero]
		if randint(1,4+couple[1])==2:
			print ('L\'eleve '+couple[0]+' a ete choisi.')
			print ('Est-ce que '+couple[0]+' a rendu sa copie ? ( o / n )')
			reponse=raw_input()
			if reponse.lower()=='o':
				listeElevesChoisis=listeElevesChoisis+[[couple[0],couple[1]+1]]
				listeNumeros=listeNumeros+[numero]
				tmp3=tmp3+[[couple[0],couple[1]]]
				b=-1
				print ('')
				
print ('Recapitulatif des eleves choisis : ')
print ('')
for i in listeElevesChoisis:
	print (i[0])

del tmp1,tmp2
fichier.close()

i=0
copie.write('# -*- coding: cp1252 -*-'+'\n')
while i<len(listeElevesChoisis):
	tmp=listeElevesChoisis[i]
	copie.write(str(tmp[0])+' '+str(tmp[1])+'\n')
	i=i+1
for i in liste:
	if i not in tmp3:
		copie.write(str(i[0])+' '+str(i[1])+'\n')

del tmp3,listeElevesChoisis,tmp
copie.close()

ancienNom='copie.txt'
nouveauNom='liste.txt'
os.remove(nouveauNom)
os.rename(ancienNom,nouveauNom)
