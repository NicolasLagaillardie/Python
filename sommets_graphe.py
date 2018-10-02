def sommets(graphe,v):
	print 'Les sommets accessibles au sommet ',v,' sont : ',
	liste=graphe[v]
	for i in range(0,len(liste)):
		print liste[i],', ',
