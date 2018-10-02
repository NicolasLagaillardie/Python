# -*- coding: cp1252 -*-

def Tri_Selection(l):
    """ Tri Selection - O(n^2) """
    for i in xrange(len(l)-1):
        mini=i
        for j in xrange(i+1,len(l)):
            if l[j]<l[mini]: mini=j
        Swap(l,i,mini)