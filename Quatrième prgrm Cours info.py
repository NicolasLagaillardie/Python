def f(n,m):	#Programme permettant de définir la parité de n ou m en fonction du fait que n soit strictement supérieur à m ou non
	s="pair"
	if n<m:
		if m%2==0:
			return s	#retourne pair
		else:
			return "im"+s	#retourne impair
	else:
		if n%2==0:
			return s
		else:
			return "im"+s