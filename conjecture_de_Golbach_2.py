def conjecture_de_Goldbach_1(a):
	import math
	
	#Création du tableau de nombres pairs
	
	t=[]
	for i in range(2,a,2):
		t.extend([i])
	print(t)
	
	#Création du tableau de nombres premiers
	
	tt=[]
	for i in range(2,a):
		vrai=0
		for j in range(2,int(math.sqrt(i))+1):
			if (i%j)==0:
				vrai=1
		if vrai==0:
			tt.extend([i])
	#Algoritme
	
	b=0
	while :