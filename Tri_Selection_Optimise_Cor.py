# -*- coding: cp1252 -*-

def Tri_Selection_Optimise(l):
    """ Tri Selection - O(n^2) """
    for i in xrange(len(l)-1):
        mini=i
        lmini = l[i]
        for j in xrange(i+1,len(l)):
            if l[j]<lmini:
                mini=j
                lmini = l[j]
        l[mini], l[i] = l[i], lmini