def degre(graphe):
	deg=0
	for i in range(0,len(graphe)):
		if len(graphe[i])>deg:
			deg=len(graphe[i])
	print 'Le degre du graphe est de ',deg
