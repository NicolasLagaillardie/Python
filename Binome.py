def binomial_rec(n,p):
	if p==0 or p==n:
		return 1
	return binomial_rec(n-1,p-1)+binomial_rec(n-1,p)
