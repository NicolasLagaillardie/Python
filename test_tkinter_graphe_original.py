from Tkinter import *
from random import randint
from math import *
 
def tafonction():
    # juste pour simuler ta fonction : creation de x, y aleatoire avec randint
    x = 200*cos(3.14159*randint(0, 800)/800)+300
    y = 200*sin(3.14159*randint(0, 600)/600)+300
    return x, y
 
def Traitement():
 
    listepoint = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19')
    listepoids = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T')
     
    for point in listepoids:
        # Sauvegarde des points precedents
        try:
            if x: # Si x existe deja : donc pas le premier point
                ancienx = x # On garde les x, y
                ancieny = y # du point precedent
        except:
            pass # Sinon c'est le premier point
 
        x, y = tafonction() # Recuperation des nouveaux x, y suivant la fonction tafonction()
 
        # On trace les lignes
        try:
            if ancienx:
                # Si ce n'est pas le premier point on trace une ligne
                cv.create_line((ancienx, ancieny),(x,y))
                # Mise en place du texte au dessus ou en dessous suivant if ancieny > y
                if ancieny > y:
                    #cv.create_text(x, y-10 , text=listepoint[listepoint.index(point)-1])
                    cv.create_text(x, y-10 , text=listepoids[listepoids.index(point)-1])
                    cv.create_text(int((ancienx+x)/2)-10, int((ancieny+y)/2)-20 , text=listepoids[listepoids.index(point)-1])
                else:
                    #cv.create_text(x, y+10 , text=listepoint[listepoint.index(point)-1])
                    cv.create_text(x, y+10 , text=listepoids[listepoids.index(point)-1])
                    cv.create_text(int((ancienx+x)/2)+10, int((ancieny+y)/2)+20 , text=listepoids[listepoids.index(point)-1])
        except:
            pass # C'est le premier point
 
# Interface
master = Tk()
cv = Canvas(master, width=800, height=600)
cv.pack()
Button(master, text="Quitter", command = master.destroy).pack()
Traitement()
mainloop()
