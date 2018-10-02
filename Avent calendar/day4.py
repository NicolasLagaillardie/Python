# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 15:03:05 2017

@author: Lagai
"""

from copy import deepcopy

f = open("day4.txt","r")
docint = f.readlines()
doc = []
for i in docint :
    doc = doc + [i[:-1].split()]
    
s = 0
c = 0

for i in doc :
    for j in i :
        inte = deepcopy(i)
        inte.remove(j)
        for l in inte :
            if len(j) == len(l) :
                inteL = list(l)
                for k in j :
                    if k in inteL :
                        inteL.remove(k)
                if inteL == [] :
                    c += 1
                    print j,l
        if c > 0 :
            c = 0
            s += 1
            break

print len(doc)-s

f.close()