def triparselec(t):
	from echangevar import echangevar
	for i in range(len(t)-1):
		cle=t[i]
		for k in range(i,len(t)):
			if t[k]<=cle:
				cle=t[k]
				num=k
		t[num],t[i]=echangevar(t[num],t[i])
	return t
