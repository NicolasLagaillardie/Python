p=input('p ?')
n=input('n ?')
q=0
while p*(q+1)<=n:
	q=q+1
print 'Le quotient de la division de ',n,' par ',p,' est : ',q
print 'Le reste de la division de ',n,' par ',p,' est : ',n-p*(q)