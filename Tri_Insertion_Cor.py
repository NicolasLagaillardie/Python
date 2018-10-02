# -*- coding: cp1252 -*-

def Tri_Insertion(l):
    """ Tri Insertion - O(n^2) """
    for i in xrange(len(l)):
        m=l[i]
        for j in xrange(i+1):
            if m<l[j]:
                for k in reversed(xrange(j+1,i+1)):
                    l[k]=l[k-1]
                l[j]=m
                break