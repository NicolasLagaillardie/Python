def verifie(valeur,tableau):
	vrai=1
	while vrai==1:
		vrai=0
		for i in range(0,len(tableau)):
			if valeur==tableau[i]:
				vrai=1
	return valeur
