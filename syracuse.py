#Attention ! ce programme gère certaines failles des précédents programmes grâce au bloc suivant

import os	#La compréhension de cette ligne n'est pas importante pour l'instant, elle permet simplement d'appeler une librairie, un ensemble de fonctions
syracuse=(-1)
while syracuse <= 0:
	syracuse = input("Tapez le nombre sur lequel vous voulez miser : ")
	try:
		syracuse = int(syracuse)
	except ValueError:
		print("Vous n'avez pas saisi de nombre")
		syracuse = -1
		continue
	if syracuse <= 0:
		print("Ce nombre est négatif")
			
#Fin du bloc d'acquisition
#Début de la suite de Syracuse

max=syracuse	#Cette variable va servir à définir la hauteur de vol de la suite
i=1	#Cette variable va permettre de connaître la durée de vol de la suite
while syracuse!=1:	#La condition générale : tant que le nombre syracuse est différent de 1
	if syracuse%2==0:
		syracuse=syracuse/2
	else :
		syracuse=3*syracuse+1
	if syracuse>=max:	#Permet, à chaque boucle, d'avoir le maximum de l'ensemble de la suite jusqu'à cette boucle
		max=syracuse
	i+=1
	print(syracuse)	#Affiche le nombre syracuse de la présente boucle
print ("Altitude du vol : ",max)
print ("Durée du vol : ",i)

os.system("pause")	#Cette ligne permet de mettre en pause le programme et éviter qu'il ne se ferme trop rapidement