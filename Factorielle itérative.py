def facto_itera(n):	#Programme permettant de trouver la factorielle d'un nombre entier de manière itérative
	s=1
	for i in range(1,n):	#Partie importante du programme : ici, on fait 1*2*...*n
		s=s*i
	s=n*s
	return s
