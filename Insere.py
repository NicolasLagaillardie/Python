# La fonction ''insere'' prend en argument un élément x et une liste triée par ordre croissant.
# Elle insère l'élément x dans la liste
 
def insere(x,liste):
 
    if liste==[]:
        return [x]
    elif x<=liste[0]:
        return [x] + liste
    else:
        return [liste[0]] + insere(x,liste[1:len(liste)])