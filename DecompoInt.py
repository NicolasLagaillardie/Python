# -*- coding: cp1252 -*-
# décomposer 45
import copy

SOL=[] # contiendra l'ensemble des solutions
for i in range (0,46):
    SOL.append([]) # liste vide partout pour commencer

SOL[0]=[] #pour le total 0
SOL[1]=[[1]] #pour le total 1

# la récurrence est amorcée
# on va pouvoir y aller

#construit les solutions pour k à partir de celles pour k
def processdec1 (k):
    T=copy.deepcopy(SOL[k]) # récupérer les solutions précédentes
    SK=[] # pour recevoir les nouvelles solutions
    for i in range(0,len(T)):# récupérer les solutions une par une
        L=T[i]
        for j in range (0,len(L)):
            M=copy.deepcopy(L)
            M[j]=M[j]+1 # ajout d'une unité
            if (j>0) and M[j-1]<M[j]: #pour conserver la décroissance
                continue
            else:
                if M not in SK: # s'il s'agit d'une nouvelle possibilité
                    SK.append(M) # l'ajouter à celles trouvées précédemment
    M=[1]*(k+1)# que des 1 pour finir
    SK.append(M)
    SOL[k+1]=SK # mise à jour en vue du traitement suivant
    print (k+1,":",len(SK))# voir la progression
    if k>1:
        SOL[k-1]=[]#pour libérer la mémoire
    return

def processdec (): # itération de la fonction précédente
    for k in range(1,45):
        processdec1(k)
    return

def sauvesoltofic (): #sauver sur fichier
    f=open("decomp45.txt", 'w')
    for i in range(0, len(SOL[45])):
        L=SOL[45][i]
        for j in range(0, len(L)):
            f.write(str(L[j])+" ")
        f.write("\n")
    f.close()
    return


processdec()                   
sauvesoltofic()