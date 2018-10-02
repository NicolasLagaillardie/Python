def tribulle(t):
	from echangevar import echangevar
	c=1
	while c==1:
		c=0
		for i in range(len(t)-1):
			if t[i]>t[i+1]:
				t[i+1],t[i]=echangevar(t[i+1],t[i])
				c=1
	return t
