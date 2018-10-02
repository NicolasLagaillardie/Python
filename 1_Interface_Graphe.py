from Tkinter import *
from math import pi,cos,sin
# -*- coding: cp1252 -*-
##Tous les commentaires en ## sont les miens, Lockas
##Le commentaire en coding... que j'ai rajouté permet les caractères avec accent
##Programmme intéressant dans l'ensemble
##Il faudrait que tu te bases sur l'algorithme pour éviter les deux blocs avant le dernier
##Ton programme pourrait être allégé en évitant la création et l'appel à des fonctions tierces, surtout si tu ne les utilises qu'une fois
##Ton programme pourrait être amélioré si tu pouvais aussi rajouter les poids


G=b=[]
ns=0



def cercle(x,y):        #Permet de tracer un cercle pour le sommet
    can.create_oval(x-5,y-5,x+5,y+5,outline='black')        ##Pourquoi tracer des cercles ? : Encombre le graphe final
                                                            ##Ou alors, choisis une fenêtre plus grande, et encore...
    
def arete(x1,y1,x2,y2):     #Permet de tracer les arêtes
    can.create_line(x1,y1,x2,y2,fill='black')

def numero(i,x,y):      #Premet de numéroter les sommets
    can.create_text(x,y,text=i)

def pattern(tab):       #Définition de l'organisation des sommets 
    A=[]                #(Polygone régulier)
    c=2*pi/len(tab)
    if len(tab)==1:
        A=[(250,250)]
    if len(tab)>1:
        k=0
        while k<len(tab):
            x=(150*cos(k*c)+250)
            y=(150*sin(k*c)+250)
            A=A+[(x,y)]
            k+=1
    return A

def graph():            #Fonction qui trace le graphe
    coord= pattern(G)
    for i in range (0,len(coord)):
        cercle(coord[i][0],coord[i][1])
        numero(i,coord[i][0],coord[i][1]-15)
    for i in range (0,len(G)):
        for j in range(0,len(G[i])):
            k=G[i][j]
            arete(coord[i][0],coord[i][1],coord[k][0],coord[k][1])




def evaluer(event):
    global ns
    ns=int(entree0.get())
    fen0.destroy()
    

def evaluerbis(event):
    global b
    c=entree.get()
    for i in range (0,len(c)):
        try:
            b=b+[int(c[i])]
        except:
            b=b
    fen.destroy()
    




fen0=Tk()           #Première fenêtre pour choisir le nombre de sommet
fen0.title('Menu')      #Contient un Entry et un Button
chaine0=Label(fen0,text='Nombre de sommet du graphe')
chaine0.pack()
entree0=Entry(fen0)
entree0.bind('<Return>',evaluer)
entree0.pack()
b01=Button(fen0,text='Quitter',command=fen0.destroy)
b01.pack()
fen0.mainloop()


for i in range(0,ns):       #Succession de fenêtres demandant les sommets
    fen=Tk()                #liés au sommet i
    b=[]
    a="Sommets voisins de",i,"séparés par une virgule"        ##J'ai rajouté "séparés par une virgule"
    chaine=Label(fen,text=a)
    chaine.pack()
    entree=Entry(fen)
    entree.pack()
    entree.bind("<Return>",evaluerbis)
    bou=Button(fen,text='Suivant (pas de sommet voisin)',command=fen.destroy)		##Implique que ton graphe est non connexe : outil polyvalent ?
    bou.pack(padx=15,pady=15)
    fen.mainloop()
    G=G+[b]
    


if len(G)!=0:           #Fenêtre finale dans laquelle on peut tracer le graphe
    feng=Tk()           ##Et si len(G)==0 ? Rediriger ou faire un return, non ?
    can=Canvas(feng,height=500,width=500,bg='ivory')
    can.pack(side=TOP,padx=5,pady=5)
    bg1=Button(feng,text='Graphe',command=graph)		##Pourquoi ne pas afficher directement le graphe ?
    bg1.pack(side=LEFT,padx=5,pady=5)
    bg2=Button(feng, text='Quitter',command=feng.quit)
    bg2.pack(side=RIGHT,padx=5,pady=5)
    feng.mainloop()
    feng.destroy()
