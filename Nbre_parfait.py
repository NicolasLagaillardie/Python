#!/usr/bin/env python 
# -*- coding: utf-8 -*-  

print("Affichage des nombres parfaits inférieurs ou égaux à un nombre entier strictement positif\n") 

n = int(input("Entrez un nombre positif:")) 
while(n<=0): 
    print("Pas de nombre négatif ou nul") 
    n = int(input("Entrez un nombre positif:")) 

np=0 
a=0 
c=0 

while(np<n): 
    np = np+1   #chaque nombre np sont vérifier dans une bouche pour savoir s'ils sont parfait 
    while(a<np-1): 
        a = a+1      #a est un compteur pour vérifier les entier d'un nombre 
        b = np%a      #b est le vérificateur de diviseur entier 
        if(b==0): 
            c = a+c      #c est la somme des diviseurs du nombre np 
    if(c==np): #si la somme des diviseurs du np = np c'est un nombre parfait 
        print(np,end = " ") 
    a = 0 #reset la valeur de a et c pour l'évaluation du prochain nombre np 
    c = 0 



input("\n\nTapez sur une touche pour quitter!") 
