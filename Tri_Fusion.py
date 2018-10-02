def Tri_Fusion(A,i=0,j="1"):

	#Bon
	
	if j=="1":
		j=len(A)-1
	if len(A)==0:
		return A
	if len(A)==1:
		if A[0]<A[1]:
			A.append(A[0])
			del A[0]
			return A
		else:
			return A
	if j>i:
		k=int((i+j)/2)
		Tri_Fusion(A,i,k)
		Tri_Fusion(A,k+1,j)
		
	#Bon
	
		Fusionner(A,i,k,j) # A préciser !
		
		Fusionner(A,i,k,j)
		l=0
		while l==0:
			if A[i]>=A[k+1] and j<=k:
				i=i+1
			elif A[i]<A[k+1] and j<=k:
				k=k+1
			elif j>k:
				l=1