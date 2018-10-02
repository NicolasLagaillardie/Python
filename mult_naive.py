def mult_naive(poly1,poly2):
	""" A revoir """
	tabtot1=[]
	for i in range(len(poly1)):
		tabint=[]
		for j in range(len(poly2)):
			tabint.extend([poly2[j]*poly1[i]])
		tabtot1.extend([tabint])
	tabtot2=[]
	for i in range(0,len(tatbot1)/min(len(poly1,poly2))):
		for j in range(i,len(tatbot1)/min(len(poly1,poly2))):
			
	return tabtot1