import os
from  random  import randrange
m=input("taille du tableau T = ")
m=int(m)
n=input("taille du tableau B = ")
n=int(n)
k=input("taille du tableau C = ")
k=int(k)

#Création des tableaux

B=[]
C=[]
T=[]
for i in range(0,m):
     T.extend([randrange(11)])
for j in range(0,n):
     B.extend([randrange(11)])
for i in range(0,k):
     C.extend([randrange(11)])
	 
#Début du dénombrement

for j in range(0,m-1):
	C[T[j]]=C[T[j]]+1
for i in range(1,k-1):
	C[i]=C[i]+C[i+1]
for j in range(0,n-1):
	B[c[j-1]]=T[j]
	C[j]=C[j]-1
T=B

os.system("pause")

#Complexité en (n+k)
