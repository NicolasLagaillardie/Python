#Ce programme permet de connaître le nombre de chiffres avant et après la virgule pour un nombre donné
#OK pour Python 3.3

import os

n=input("Nombre à dénombrer : ")
m=p=float(n)
if m<0:
        m=-m
k=0
j=1
l=0


#Bloc suivant, utile ?

#if n==0:
#	print ("0 est un unique chiffre")
#	return 0

while m>=l:
	if l==0:
		l=1
	k=k+1
	l=l*10
	
#Partie entière OK!
	
#Fonction int() à créer : m=m-int(m) → création de la partie décimale

l=0
m=m-int(m)
print(m)
	
while m!=int(m) :
	if l==0:
		l=1
	m=m*l
	j=j+1
	l=l*10
	print(j,m)

print ("Ce nombre possède ",k," chiffre(s) après la virgule et ",j-1," décimale(s)")