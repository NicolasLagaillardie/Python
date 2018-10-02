# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:28:27 2016

@author: Nicolas
"""

def un(n,u0=9,k=0):
    if k==n :
        return u0
    else:
        return un(n,3*u0**4+4*u0**3,k+1)
        
print 'U3='+str(un(3))

def neuf(k):
    r=0
    chaine = str(k)
    for i in range(len(chaine)-1,-1,-1):
        if chaine[i] == '9' :
            r=r+1
        else:
            return r
    return r
    
for i in range(10):
    print 'C'+str(i)+'='+str(neuf(un(i)))
    

def precedent(k):
    chaine = str(k)
    for i in range(len(chaine)-1,-1,-1):
        if chaine[i] != '9' :
            return int(chaine[i])
    return 0
    
for i in range(10):
    print precedent(un(i))
    
def pn(k):
    return len(str(k))
    
for i in range(10):
    print pn(un(i))/(4.**i)