

def dicho(liste, elt, i=0):
    if liste ==[] :
        return False
    elif len(liste) ==1:
        return liste[0]==elt 
    else:
        pivot = len(liste)//2
        if liste[pivot]  >= elt:
            print liste[:pivot], elt, i
            return dicho (liste[:pivot], elt, i)
        else:
            print liste[pivot:], elt, i
            return dicho (liste[pivot:], elt, i+pivot)

dicho([1,2,3,4,4,5,6],3)

class poly2:
    def __init__(self, a=0, b=0, c=0) :
        self.a, self.b, self.c=a, b, c

    def affiche(self, x=0):
        print self.a*x**2+self.b*x+self.c

A=poly2(2,3,4)
A.affiche(1)
poly2().affiche() 

class Vecteur2D:
    def __init__(self, x=0,y=0):
        self.x,self.y=x,y

    def affiche(self) :
        print [self.x, self.y] 

    def somme(self, a=0, b=0) :
        print [self.x + a, self.y + b] 

B=Vecteur2D(2,3)
B.affiche()
B.somme(3,4)
ABC = 'abcdefghijklmnopqrstuvwxyz'

def vigenere(t, c) :
    return [ABC[(ord(t[k])-97+ord(c[k%len(c)])-97)%26] for k in range(len(t))] 

print vigenere('ecolepolytechnique', 'concours')

def pgcd(a,b):
    if a<b:
        a,b=b,a
    if b==a:
        return a
    else:
        return pgcd(a-b,b)
        
def pgcdM(liste):
    s=liste[0]
    for i in range(1,len(liste)):
        s=pgcd(s,liste[i])
    return s
