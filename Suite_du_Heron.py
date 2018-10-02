#Ce programme ne fonctionne correctement qu'avec Python 3.3

import os
import math

n=input("Nombre dont on veut la racine : ")
n=int(n)
racine=n/2
prec=input("Nombre de chiffre(s) après la virgule : ")
prec=int(prec)

while (racine*racine)%n>pow(10,-prec):
	racine=( racine + ( n / racine ))/2
	
print ("Racine de ",n," = ",racine," avec une precsion de 10^(-",prec,")")