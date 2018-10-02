def connexe(graphe):
	for i in range(0,len(graphe)):
		if len(graphe[i])==0:
			return 'Faux'
	f=[]
	O=[0]
	while O<>[]:
		for i in range(g[O[0]]):
			if not(i in f or i in O):
				O=O+[i]
		f=[O[0]]+f
		O=[1:len(O)]
	if len(f)!=len(graphe):
		return 'Faux'
	return 'Vrai'