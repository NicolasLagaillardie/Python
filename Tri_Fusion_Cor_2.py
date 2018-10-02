# La fonction ''tri_fusion'' prend en argument une liste
# Elle renvoie la liste triée. Pour cela, on sépare la liste en deux, on les trie séparément puis on les fusionne grâce à la fonction ''fusion'' définie précédemment
 
def tri_fusion(liste):
 
    n=len(liste)
 
    if n==0 or n==1:
        return liste
    else:
        return fusion(tri_fusion(liste[0:n/2]),tri_fusion(liste[n/2:n]))