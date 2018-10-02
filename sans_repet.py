def sans_repet(a=3):

	#Si l'utilisateur ne rentre pas un tableau
	
	if type(a)==float or type(a)==int:
		a=int(a)
		from  random  import randrange
		t=[]
		for i in range(a):
			t.extend([randrange(11)])
	else:
		t=a
		a=len(t)
			
	#Tri tableau
	
	for j in range(1,a):
		cle=t[j]
		i=j-1
		while i>=0 and t[i]>cle:
			t[i+1]=t[i]
			i=i-1
		t[i+1]=cle
		
	#Fin tri, début programme
	
	for i in range(1,a):
		if t[i-1]==t[i]:
			return False
	return True
