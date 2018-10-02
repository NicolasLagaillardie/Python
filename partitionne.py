def partitionne(p,t):
	if len(t)==0:
		return [],[]
	else:
		print(t[0:len(t)])
		for i in range(len(t)):
			t1,t2=partitionne(p,[t[i]]) #PROBLEME !!!!
			print(t1,t2)
			if t[0]<p:
				return [t[0]]+t1,t2
			else:
				return t1,[t[0]]+t2