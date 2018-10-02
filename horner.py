def horner(poly,x):
	somme=0
	for i in range(0,len(poly)):
		j=len(poly)-i-1
		somme=somme*x+tab[j]
	return somme