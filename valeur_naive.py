def valeur_naive(poly,x):
	from math import *
	total=0
	for i in range(len(poly)):
		total=poly[i]*(x**i)+total
	return total
