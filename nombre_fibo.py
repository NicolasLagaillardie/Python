def nombre_fibo(n):
	i=j=1
	h=i+j
	g=0
	if n==0:
		print "false"
	for k in range(n):
		if n==i or n==j:
			g=1
		h=i
		i=j
		j=i+h
	if g==1:
		return "True"
	else:
		return "False"