# -*- coding: cp1252 -*-

def Tri_Insertion_Optimise(l):
    for i in xrange(len(l)):
        m=l[i]
        for j in xrange(i+1):
            if m<l[j]:
                l[j+1:i+1] = l[j:i]
                l[j]=m
                break