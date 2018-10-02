def print_poly(t):
	if t[0]!=0:
		print t[0],'X',
	for i in range(1,len(t)):
		if t[i]>0:
			print '+',t[i],'X',i,
		elif t[i]<0:
			print t[i],'X',i,