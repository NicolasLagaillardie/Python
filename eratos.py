def eratos(n):
	t=[False,False]
	for i in range(2,math.sqrt(n)):
		if (a%i)==0:
			t.extend([True])
		else:
			t.extend([False])