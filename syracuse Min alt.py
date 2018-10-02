def u1AltMin(m):	#Ce programme permet de définir la hauteur de vol mini pour un nombre n injecté dans la suite de Syracuse tel que mini soit au moins m fois supérieur à n

	#Bloc de vérfication
		try:
			m=int(m)
		except ValueError:
			m=(-1)
			while m<=0:
				try:
					m=int(m)
				except ValueError:
					print("Vous n'avez pas saisi de nombre")
					m=-1
					continue
				if m<=0:
					print("Ce nombre est négatif")
			
	#Fin du bloc

	n=0
	mini=m
	while m*n<=mini:	#Boucle qui se répète tant que...
		n=+1
		syracuse=n
		mini=syracuse
		while syracuse!=1:	#Suite de Syracuse
			if syracuse%2==0:
				syracuse=syracuse/2
			else :
				syracuse=3*syracuse+1
			if syracuse>=mini:
				mini=syracuse
	print ("Nombre initial : ",n," Hauteur de vol minimale : ",mini)
