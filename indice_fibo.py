def indice_fibo(a):
	i=j=1
	h=i+j
	for k in range(a):
		if a==i or a==j:
			return i
		h=i
		i=j
		j=i+h
	return -1
