def chemin(graphe,u,v):
	if len(graphe[u])==0 or len(graphe[v])==0:
		return 'Faux'
	f=[]
	O=[0]
	while O<>[]:
		for i in range(g[O[0]]):
			if not(i in f or i in O):
				O=O+[i]
				d[i]=d[O[0]]+1
		f=[O[0]]+f
		O=[1:len(O)]
	return 'Vrai'