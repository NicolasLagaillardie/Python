#Affichage du triangle de Pascal
#Python 2.7

rang='a'
while type(rang)!=int or rang<0:
	print 'Jusqu\'ра quel n voulez-vous afficher le triangle de Pascal'
	rang=input()
	print ''

tableau=[[1]]

for i in range(0,rang):
	tmp=[]
	curseur=tableau[i]
	for k in range(0,len(curseur)-1):
		tmp=tmp+[curseur[k]+curseur[k+1]]
	tmp=[1]+tmp+[1]
	tableau=tableau+[tmp]

for n in tableau:
	for k in n:
		print k,' ',
	print ''
