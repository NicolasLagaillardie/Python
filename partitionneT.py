def partitionne(p,t):
	if len(t)==0:
		return [],[]
	else:
		t1,t2=partitionne(p,t[0:len(t)])
		if t[0]<p:
			return [t[0]]+t1,t2
		else:
			return t1,[t[0]]+t2
