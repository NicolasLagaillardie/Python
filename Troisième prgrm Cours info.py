#Comparaison de deux porgrammes avec une indentation différente

#On demande les variables, pour créer un programme viable
 n=input("N ?")
 m=input("M ?")
 n=int(n)
 m=int(m)
 
#Premier programme
if n==0:
	n=1
	if m==0:
		m=2*n
	else:
		m=n-1
		
#Second programme
if n==0:
	n=1
	if m==0:
		m=2*n
else:	#Remarquons l'indentation différente
	m=n-1
	
#Le premier programme ne modifie m que si n=0. Si c'est le cas, alors il modifie m en fonction des conditions du bloc

#Le second modifie m en fonction du fait que n soit égal ou non à 0