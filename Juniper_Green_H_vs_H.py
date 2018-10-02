# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:31:13 2013

@author: Nicolas
"""

# Juniper Green(B)
# Si le premier joueur donne un nombre premier >B/2 ,
# le second joueur ne peut rien faire

def jeu(entier,B,affiche=1):
	if entier<0 or entier>B:
		return []
	MuDi=[]
	for i in range(1,entier):
		if entier%i==0:
			MuDi.extend([i])
	for i in range(2,B):
		if i*entier<=B:
			MuDi.extend([i*entier])
		else:
			break
	if affiche==1:
		print 'Multiples et diviseurs de ',entier,' : ',
	return MuDi
	
def CoupsJouables(listeCoupsJoues,B):
    coups=jeu(listeCoupsJoues[len(listeCoupsJoues)-1],B,0)
    for i in range(0,len(coups)):
        if coups[i] in listeCoupsJoues:
            coups[i]=-1
        coups2=[]
        for i in range(0,len(coups)):
            if coups[i] != -1:
                coups2.extend([coups[i]])
    return coups2
	
def JuniperGreen(B=100):
    """(B)=(limite d'intervalle)"""
    debut=0 # Var pour la condition de début
    match=0 # Var de maintien du jeu
    joueurActuel=1
    joueurSuivant=2
    listeCoupsJoues=[]
    while match==0:
        print 'Joueur actuel : ',joueurActuel
        if debut==0:    # Regle du début
            limite=int(float(B)/float(2))
            debut=1
        else:
            limite=B
        nombreJ=limite+1
        aide=1
        while nombreJ<1 or nombreJ>limite:
            print 'Selectionnez un nombre entre 1 et ',limite
            nombreJ=raw_input()
            try:
                nombreJ=int(nombreJ)
            except:
                nombreJ=-1
            if len(listeCoupsJoues)>0:  # Règle principale du jeu :
            # ne sont jouables que les diviseurs
            # et multiples du dernier nombre joué
                if nombreJ not in CoupsJouables(listeCoupsJoues,B):
                    nombreJ=limite+1
                if aide>=3:
                    print 'Liste de coups disponibles : ',CoupsJouables(listeCoupsJoues,B)
                    aide=aide-1
                    print ''
            aide=aide+1
        listeCoupsJoues.extend([nombreJ])
        joueurSuivant,joueurActuel=joueurActuel,joueurSuivant
        print 'Liste de coups joués : ',listeCoupsJoues
        print ''
        listeCoupsJouables=CoupsJouables(listeCoupsJoues,B)
        if len(listeCoupsJoues)==B or len(listeCoupsJouables)==0:
        # Condtion de sortie du jeu
            match=1
    print ''
    print 'Le jeu est finit, le joueur ',joueurSuivant,' a gagné'
    print ''
    print 'Voulez vous recommencer une autre partie ? y or n'
    reponse=raw_input()
    reponse=reponse.lower()
    if reponse=='y':
		B=-1
		while B<1:
			print 'Veuillez choisir une limite'
			B=raw_input()
			try:
				B=int(B)
			except:
				B=-1
		JuniperGreen(B)

JuniperGreen(100)