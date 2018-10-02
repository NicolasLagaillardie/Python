def mult_naive_cor(poly1,poly2):
	c=[0 for i in range(0,len(poly1)+len(poly2)-1)]
	for i in range(0,len(poly1)):
		for j in range(0,len(poly2)):
			c[i+j]=c[i+j]+poly1[i]*poly2[j]
	return c
