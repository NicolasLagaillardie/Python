def est_premier(n):
	for i in range(2,math.sqrt(n)):
		if (a%i)==0:
			return False
	return True