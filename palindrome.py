def palindrome(n=3):


	if type(n)==float or type(n)==int:
			n=int(n)
			from  random  import randrange
			t=[]
			for i in range(n):
				t.extend([randrange(11)])
	else:
		t=n
		n=len(t)
		
		
	k=int(len(n)/2)
	for i in range(0,k-1):
		if  n[i]!=n[len(n)-1-i]:
			return False
	return True