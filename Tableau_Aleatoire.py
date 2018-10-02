def tableaurand(n,p=-1):
	if p==-1:
		p=n
	from random import randint
	t=[]
	for i in range(1,n):
		t.extend([randint(0,p)])
	return t
