def membre_rapide(m,a):
	import os
	from  random  import randrange
	t=[]
	for k in range(0,m-1):
		t.extend([randrange(11)])
	for j in range(1,m-1):
		cle=t[j]
		i=j-1
		while i>=0 and t[i]>cle:
			t[i+1]=t[i]
			i=i-1
		t[i+1]=cle
	while 