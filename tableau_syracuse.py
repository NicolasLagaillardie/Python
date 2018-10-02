def tableau_syracuse(k):	#Programme annexe, qui crée une matrice de k colonnes et 1 ligne à 2 valeurs :durée et altitude
	t=k*[(0,0)]
	for m in range(1,k):
		i=1
		maxi=syracuse
		while syracuse!=1:
			if syracuse%2==0:
				syracuse=syracuse/2
			else :
				syracuse=3*syracuse+1
			if syracuse>=maxi:
				max=syracuse
			i+=1
		t[m]=(i,maxi)
