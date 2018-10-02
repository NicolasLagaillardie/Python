#Suite de Fibonacci itérative
def Suite_Fibo_I(n):
	t=[1,1]
	for i in range(2,n):
		t.extend([t[i-1]+t[i-2]])
	return t
