def degre(t):
	if len(t)==0:
		return -1
	j=len(t)-1
	for i in range(len(t)-1,0,-1):
		if t[i]==0:
			j=j-1
		else:
			return j