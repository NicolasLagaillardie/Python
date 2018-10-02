# -*- coding: cp1252 -*-
#Juniper Green(B)
#Si le premier joueur donne un nombre premier >B/2 , le second joueur ne peut rien faire
from random import randint

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
	if listeCoupsJoues!=[]:
		coups=jeu(listeCoupsJoues[len(listeCoupsJoues)-1],B,0)
		for i in range(0,len(coups)):
			if coups[i] in listeCoupsJoues:
				coups[i]=-1
		coups2=[]
		for i in range(0,len(coups)):
			if coups[i] != -1:
				coups2.extend([coups[i]])
		return coups2
	else:
		coups=[]
		for k in range(1,B):
			coups.extend([k])
		return coups

def JuniperGreenComputerRecu(listeCoupsJoues,B,time):   #Très lourd car IA
	if time==0:
		listedispo=CoupsJouables(listeCoupsJoues,B)
		return listedispo[randint(1,len(listedispo)-1)]
	j=0
	ordreFinal=[(len(CoupsJouables(listeCoupsJoues,B)),listeCoupsJoues)]
	while j<=time:
		ordreInter=[]
		for i in ordreFinal:
			ordreInter.extend([i])
		for i in ordreFinal:
			listeInter=CoupsJouables(i[1],B)
			for k in listeInter:
				listecoupsJouesInter=i[1]+[k]
				ordreInter.extend([(len(CoupsJouables(listecoupsJouesInter,B)),listecoupsJouesInter)])
		ordreInter2=[]
		for i in ordreInter:
			if i[0]==0 and int(float((len(i[1])-len(listeCoupsJoues)))%float(2))!=0:
				if 1 not in i[1]:
					if len(i[1])>len(listeCoupsJoues)+j:
						ordreInter2.extend([i])
			elif i[0]!=0:
				if 1 not in i[1]:
					if len(i[1])>len(listeCoupsJoues)+j:
						ordreInter2.extend([i])
		if ordreFinal==ordreInter2:
			j=time+1
		else:
			ordreFinal=ordreInter2
			j=j+1

	try:
		if min(ordreFinal):
			if int(float(time)%float(2))==0:
				minima=max(ordreFinal)
			else:
				minima=min(ordreFinal)
			listesommets=minima[1]
			return listesommets[len(listeCoupsJoues)]
	except:
		return JuniperGreenComputerRecu(listeCoupsJoues,B,time-1)
		
def JuniperGreenComputer(listeCoupsJoues,B,time):   #Lourd car IA
	listedispo=CoupsJouables(listeCoupsJoues,B)
	if len(listedispo)==1:
		return listedispo[0]
	ordre1poidss=[]
	i=0
	for test in listedispo:    # Rôle ?
		listeO1=CoupsJouables(listeCoupsJoues+[test],B)
		ordre1poidss.extend([(len(listeO1),i)])
		i=i+1
	minima=min(ordre1poidss)
	
	if minima[0]!=0:
		return JuniperGreenComputerRecu(listeCoupsJoues,B,time)
	else:
		return listedispo[minima[1]]
	
def JuniperGreen(B=100):
    """(B)=(limite d'intervalle)"""
    debut=0
    print 'Voulez-vous être le premier joueur, le second joueur ou le spectateur? (1, 2 ou 3)'
    verif=0
    while verif==0:
        verif=raw_input()
        try:
            verif=int(verif)
        except:
            verif=-1
        if verif==1:
            print 'Vous êtes le premier joueur'
        elif verif==2:
            print 'Vous êtes le second joueur'
        elif verif==3:
            print 'Vous êtes spectateur'
        else:
            print 'Veuillez sélectionner un numéro de joueur valide'
            verif=0
    print ''
    
    print 'Quelle difficulté voulez-vous ? A partir de 0'
    time=-1
    while time<0:
        time=raw_input()
        time=int(time)
        if time>=0:
            print 'Vous avez choisi une difficulté de : ',time
        else:
            print 'Veuillez sélectionner une difficulté valide'
            time=-1
    print ''
    
    match=0
    if verif==1:
        listeCoupsJoues=[]
        joueurSuivant=2
        joueurActuel=1
    else:
        print 'Joueur actuel : 1'
        joueurActuel=2
        listeCoupsJoues=[]
        nombreO=JuniperGreenComputer(listeCoupsJoues,int(float(B)/float(2)),0)
        debut=1
        print 'Je choisi le nombre : ',nombreO
        listeCoupsJoues.extend([nombreO])
        joueurSuivant=1
        print ''
    while match==0:
        print 'Joueur actuel : ',joueurActuel
        if debut==0:
            limite=int(float(B)/float(2))
            debut=1
        else:
            limite=B
            if (joueurActuel==1 and verif==1) or (joueurActuel==2 and verif==2):
                if verif==2:
                    joueurActuel=1
                    joueurSuivant=2
                nombreJ=limite+1
                aide=1
                while nombreJ<1 or nombreJ>limite:
                    print 'Selectionnez un nombre entre 1 et ',limite
                    nombreJ=raw_input()
                    try:
                        nombreJ=int(nombreJ)
                    except:
                        nombreJ=-1
                    if len(listeCoupsJoues)>0:
                        if nombreJ not in CoupsJouables(listeCoupsJoues,B):
                            nombreJ=limite+1
                    if aide>=3:
                        print 'Liste de coups disponibles : ',CoupsJouables(listeCoupsJoues,B)
                        aide=aide-1
                        print ''
                    aide=aide+1
                listeCoupsJoues.extend([nombreJ])
                if verif==1:
                    joueurActuel=2
                    joueurSuivant=1
				
            else:
                if verif==2:
                    joueurActuel=2
                    joueurSuivant=1
                elif verif==3 and joueurActuel!=1:
                    joueurActuel=1
                elif verif==3 and joueurActuel!=2:
                    joueurActuel=2
                if verif==3 and time==-1:
                    timeL=randint(0,3)
                    nombreO=JuniperGreenComputer(listeCoupsJoues,B,timeL)
                elif verif==3 and time!=-1:
                    nombreO=JuniperGreenComputer(listeCoupsJoues,B,time)
                else:
                    nombreO=JuniperGreenComputer(listeCoupsJoues,B,time)
                listeCoupsJoues.extend([nombreO])
                print 'Je choisi le nombre : ',nombreO
                if verif==1:
                    joueurActuel=1
                    joueurSuivant=2
                elif verif==3 and joueurSuivant!=1:
                    joueurSuivant=1
                elif verif==3 and joueurSuivant!=2:
                    joueurSuivant=2
        print 'Liste de coups joués : ',listeCoupsJoues
        print ''
        listeCoupsJouables=CoupsJouables(listeCoupsJoues,B)
        if len(listeCoupsJoues)==B or len(listeCoupsJouables)==0:
            match=1
    print ''
    print 'Le jeu est finit, le joueur ',joueurSuivant,' a gagné en ',len(listeCoupsJoues),' coups'
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