def pgcdrec(a,b):
	if b==0:
		return a
	return pgcdrec(b,a%b)
