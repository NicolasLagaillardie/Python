def facto_recurs(n):	#Programme permettant de trouver la factorielle d'un nombre entier de manière récursive
	if n==0:	#0!=1
		return 1
	else:	#Partie importante du programme : ici, on fait n! = n*((n-1)!) puis (n-1)! = (n-1)*((n-2)!) jusqu'à (n-(n-2))! = (n-(n-2))*(1!)
		return n*facto_recurs(n-1)