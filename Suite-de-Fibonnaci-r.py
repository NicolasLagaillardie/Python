#Suite de Fibonacci récursive
def Suite_Fibo_R(n):
	if n<=1:
		return 1
	else:
		return Suite_Fibo_R(n-2)+Suite_Fibo_R(n-1)