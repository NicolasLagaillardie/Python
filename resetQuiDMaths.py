#Permet de reinitialiser le fichier liste.txt

# -*- coding: cp1252 -*-
# -*- coding: latin-1 -*-

import os

fichier=open("liste.txt","r")
copie=open("copie.txt","w")
	
liste=fichier.read()
liste=liste.split("\n")

tmp1=[]
for i in liste:
        i=i.split(" ")
        tmp1=tmp1+i

tmp2=[]
b=5
while b>0:
	try:
		tmp2=tmp2+[[tmp1[b]+" "+tmp1[b+1],int("0")]]
		b=b+3
	except:
		b=-1

fichier.close()

copie.write("# -*- coding: cp1252 -*-"+"\n")
for i in tmp2:
	copie.write(str(i[0])+" "+str(i[1])+"\n")

del tmp1,tmp2,liste
copie.close()

ancienNom="copie.txt"
nouveauNom="liste.txt"
os.remove(nouveauNom)
os.rename(ancienNom,nouveauNom)
