import os
from  random  import randrange
m=input("m=")
m=int(m)
t=[]
for k in range(0,m-1):
	t.extend([randrange(11)])
print "tableau initial : ",t
for j in range(1,m):
	cle=t[j]
	i=j-1
	while i>=0 and t[i]>cle:
		t[i+1]=t[i]
		i=i-1
	t[i+1]=cle
print"tableau final : ",t
os.system ("pause")

##Si la liste est dans l'ordre croissant, nous sommes dans le meilleur cas, la complexité est de (n)

#Si la liste est dans l'ordre décroissant, nous sommes dans le pire cas, la complexité est de (n^2)

#Dans le cas moyen, la complexité est de (n^2)

#Cet exemple montre bien pourquoi on préfère exprimer la complexité d'un programme dans le pire cas
