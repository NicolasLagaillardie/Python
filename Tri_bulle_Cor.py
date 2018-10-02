# -*- coding: cp1252 -*-

def Tri_Bulle(l):
    """ Tri bulle - O(n^2)"""    
    for i in xrange(len(l)):
        for j in reversed(xrange(i,len(l))):
            if l[j]<l[j-1]:
                t=l[j]
                l[j]=l[j-1]
                l[j-1]=t