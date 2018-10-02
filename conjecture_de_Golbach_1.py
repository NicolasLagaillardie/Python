def conjecture_de_Goldbach_1(a):
	import math
	t=[]
	tt=[]
	for i in range(2,a-1):
		vrai=0
		for j in range(2,int(math.sqrt(i))+1):
			if (i%j)==0:
				vrai=1
		if vrai==0:
			t.extend([i])
	for i in range(0,len(t)):
		for j in range(0,len(t)):
			tt.extend([t[i]+t[j]])
	for j in range(1,len(tt)):
		cle=tt[j]
		i=j-1
		while i>=0 and tt[i]>cle:
			tt[i+1]=tt[i]
			i=i-1
		tt[i+1]=cle
	l=len(tt)-3
	i=0
	while i<=l:
		l=len(tt)-3
		if tt[i]==tt[i+1]:
			del tt[i]
			i=i-1
		i=i+1
	l=len(tt)-2
	i=0
	while i<=l:
		l=len(tt)-2
		if tt[i]%2!=0:
			del tt[i]
		i=i+1
	for i in range(0,len(tt)-1):
		if tt[i]+2!=tt[i+1]:
			print("A l'indice : ",i,", il manque le nombre : ",tt[i]+2)
			return False
	return True
