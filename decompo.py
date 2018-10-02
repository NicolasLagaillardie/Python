def decompo(n):
	if n==0:
		return [0]
	t=[]
	for i in range(0,n):
		tvaleurs=[]
		for k in range(0,i):
			while