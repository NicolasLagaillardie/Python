def arbre(graphe):
	import connexe
	if connexe(graphe)=='Faux':
		return 'Faux'
	else:
		arrete=0
		for i in range(0,len(graphe)):
			arrete=arrete+len(graphe[i])
		if arrete-len(graphe)==len(graphe):
			return 'Faux'
		else:
			return 'Vrai'