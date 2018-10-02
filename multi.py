def multiplication2(a,b):
	x=0
	while b != 1:
		if b%2==1:
			a=2*a+a
		
		b=b/2
	return a