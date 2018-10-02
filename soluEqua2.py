a=0
while a==0:
	a=input('a')
b=input('b')
c=input('c')
from math import sqrt
print 'votre equation est : ',a,' * x ² + ',b,' * x + ',c,' = 0'
delta=b**2-4*a*c
if delta<0:
	print 'il n'y a pas de solution reelles'
elif delta==0:
	print 'il y a une racine double qui est : x = ',float(-b)/float(a)
else:
	print 'il y a deux racine qui sont : x1 = ',(float(-b)+sqrt(delta))/(2*float(a)),' et x2 = ',(float(-b)-sqrt(delta))/(2*float(a))