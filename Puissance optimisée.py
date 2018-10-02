def power_optimized(x,y):	#Ce programme est la fonction puissance en version optimisée : il nécessite moins d'opérations pour arriver au résultat
	if y==0:
		return 1
	elif y%2==0:	#Si y est pair
		return power_optimized(x,(y-1)/2)*power_optimized(x,abs((y-1)/2))	#a^n=(a^(n/2))^2
	else:	#Sinon
		return x*power_optimized(x,abs((y-1)/2))*power_optimized(x,abs((y-1)/2))	#a^n=a*(a^(n/2))^2