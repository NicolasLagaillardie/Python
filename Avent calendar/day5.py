# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 14:05:11 2017

@author: Lagai
"""

from copy import deepcopy

f = open("day5.txt","r")
docint = f.readlines()
doc = []

for i in docint :
    doc = doc + [int(i[:-1])]

def f(doc) :
    
    i = 0
    k = 0
    c = 0
    
    while i > -1  and i < len(doc) :
            c = deepcopy(i)
            i += deepcopy(doc[i])
            if doc[c] > 2 :
                doc[c] -= 1
            else :
                doc[c] += 1
            k += 1
    return k
            
print f(doc)