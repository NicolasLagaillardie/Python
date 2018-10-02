# La fonction ''fusion'' prend en argument deux listes triées par ordre croissant liste1 et liste2
# Elle renvoie la liste obtenue en fusionnant liste1 et liste2 de manière à ce qu'elle soit triée
 
def fusion(liste1,liste2):
 
    if liste1==[]:
        return liste2
    elif liste2==[]:
        return liste1
    else:
        return fusion(liste1[1:len(liste1)],insere(liste1[0],liste2))