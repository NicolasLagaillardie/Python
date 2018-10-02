#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from random import randint
from copy import deepcopy
from math import sqrt
from math import exp
from random import random
from matplotlib import pyplot as plt
import numpy as np

def distance(v1, v2) :
    return sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)

def longueur(listeV) :
    d = 0
    for i in range(len(listeV) - 1):
        d = d + distance(listeV[i], listeV[i+1])
    return d

def aux_recuit(listeV, delta, r):
    a = randint(0,len(listeV)-1)
    b = deepcopy(a)
     
    while b == a :
        b = randint(0,len(listeV)-1)
    
    Cprime = deepcopy(listeV) 
    Cprime[a], Cprime[b] = Cprime[b], Cprime[a]
    
    Lc1 = longueur(listeV)
    Lc2 = longueur(Cprime)
    
    if Lc2-Lc1 < 0 :
        return Cprime
    else:
        if exp(-(Lc2-Lc1)/delta) > r :
            return Cprime
        else:
            return listeV

def distotale(listeV) :

    r = 0

    for i in range(len(listeV)-1) :
        r = r + distance(listeV[i], listeV[i+1])

    r = r + distance(listeV[0],listeV[len(listeV)-1])

    return r

def recuit(listeV, delta, r, n):
    
    for i in range(n) :
        
        listeV=deepcopy(aux_recuit(listeV, delta, r)) 
        delta = random()/2.+0.5
    
    r = distotale(listeV) 
    
    #print 'liste des villes a visiter dans ordre : ',
    #print listeV
    #print' distance totale de parcours : ', 
    #print r
    return listeV
    
j = 0

l=[]
#r=20,50
#a=50,100
#b=50,100
#rappel : a(x-d)**2+2*b*(x-d)*(y-e)+c*(y-e)**2=1
a=50
b=20
c=40
d=50
e=60

while j<200:
    
    x = randint(-4*(a+d),4*(a+d))+random()
    
    if (2*b*(x-d)-2*c*e)**2-4*(a*(x-d)**2+2*b*(d-x)*e+c*e**2-1)*c >=0 :
        
        y1 = (-(2*b*(x-d)-2*c*e)+sqrt((2*b*(x-d)-2*c*e)**2-4*(a*(x-d)**2+2*b*(d-x)*e+c*e**2-1)*c))/(2.*c)
        y2 = (-(2*b*(x-d)-2*c*e)-sqrt((2*b*(x-d)-2*c*e)**2-4*(a*(x-d)**2+2*b*(d-x)*e+c*e**2-1)*c))/(2.*c)
        
        if [x,y1] not in l :
        
            l.append([x,y1])
        
            j += 1
            
        if [x,y2] not in l :
        
            l.append([x,y2])
        
            j += 1    
    

liste = recuit(l,4,0.001,100000)
X = [i[0] for i in liste]+[liste[0][0]]
Y = [i[1] for i in liste]+[liste[0][1]]
x = np.array(X)
y = np.array(Y)

plt.plot(x,y)
plt.show()

"""partie fonctions"""

def recuit_fonction_1D(f,a,b,delta,n):
    
    print 0
    