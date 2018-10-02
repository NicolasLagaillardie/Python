#Eratosthène

def Erato(n):

	#Tableau Initial
	
	t=[]
	for i in range (0,n+1):
		t.extend([i])
		
	#Traitement du tableau
		
	for i in range (2,len(t)-1):
		for k in range (i+1,len(t)):
			if t[i]!=0:
				if t[k]%t[i]==0:
					t[k]=0
	t.remove(1)
	t=[x for x in t if x!= 0]
	
	#OK !
	
	return t
