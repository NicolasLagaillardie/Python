def syracuse_test(m):	#Ce programme permet d'afficher les caractéristiques des m nombres entiers injectés dens la suite de Syracuse
	for syracuse in range(1,m):	#Boucle qui permet de tester tous les nombres entiers de 1 à m
		n=syracuse
		maxi=syracuse
		i=1
		while syracuse!=1:	#Boucle de Syracuse
			if syracuse%2==0:
				syracuse=syracuse/2
			else :
				syracuse=3*syracuse+1
			if syracuse>=maxi:
				maxi=syracuse
			i+=1
		print ("Nombre : ",n," Altitude du vol : ",maxi," Duree du vol : ",i)
