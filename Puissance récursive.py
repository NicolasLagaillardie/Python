def power_recurs(x,y):	#Ce programme est le fonction récursive puissance faite de manière intuitive : x^y=x*x*x*...*x y fois	
	if y==0:
		return 1
	else:	#Partie important du programme
		return x*power_recurs(x,y-1)