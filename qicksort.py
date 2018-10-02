def quicksort(t):
	from partitionne import partitionne
	if len(t)<=1:
		return t
	else:
		t1,t2=partitionne(t[0],t)
		print(t1)
		print(t2)
		return quicksort(t1)+quicksort(t2)
