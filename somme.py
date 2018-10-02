def somme(poly1,poly2):
	t=[]
	taille=min(len(poly1),len(poly2))
	for i in range(taille):
		t.extend([poly1[i]+poly2[i]])
	if taille==len(poly1):
		maxi=poly2
	else:
		maxi=poly1
	for j in range(i+1,len(maxi)):
		t.extend([maxi[j]])
	return t
