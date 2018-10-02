def conjecture_de_Golbach(n):
	if n<2:
		return False
	if n==2:
		return 2
	import math
	import threading
	pairs=[]
	premiers=[]
	# Tableau des nombres pairs
	for i in range(4,n,2):
		pairs.extend([i])
	print(pairs,len(pairs))
	# Tableau des nombres premiers
	for i in range(2,n):
		premier=0
		for j in range(2;math.sqrt(i)): # Boucle qui peut être très lourde
			if (i%j)==0:
				premier=1
				continue
		if premier==0:
			premiers.extend([i])
	print(premiers,len(premiers))

	# Fonction pour Golbach
	
	for i in range(0,len(pairs)-1):
		Vrai=0
		while Vrai==0:
						
			


			if :
				return False
