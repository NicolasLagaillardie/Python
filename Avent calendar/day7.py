# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 14:46:10 2017

@author: Lagai
"""

from copy import deepcopy
import time


f = open("day7.txt","r")

docint = f.readlines()
leafI = []
pred = []
w = []

for i in docint :
    inte = [i[:-1]]
    if ' -> ' in inte[0] :
        inte2 = inte[0].split(' -> ')
        leafI = leafI + [inte2[1].split(',')]
        inte3 = inte2[0].split(' (')
        pred = pred + [inte3[0]]
        w = w + [int(inte3[1][:-1])]
    else :
        leafI = leafI + [[]]
        inte3 = inte[0].split(' (')
        pred = pred + [inte3[0]]
        w = w + [int(inte3[1][:-1])]

leaf = [[]] * len(leafI) 

for i in range(0,len(leafI)) :
    if len(leafI[i]) > 0 :
        leaf[i] = leaf[i] + [leafI[i][0]]
        for j in leafI[i][1:] :
            leaf[i] = leaf[i] + [j[1:]]

p = 0

for i in leaf :
    if len(i) != 0 :
        start = deepcopy(i)
        break
    else :
        p += 1

while p != len(leaf) :
    inte = pred[p]
    p = 0
    for i in leaf :
        if inte in i :
            start = deepcopy(i)
            break
        else :
            p += 1
         


def niveau(leaf,pred,start,lvl):
    if leaf[start] == [] :
        return lvl
    else :
        l = []
        for i in leaf[start] :
            for j in  range(0,len(pred)) :
                if pred[j] == i :
                    l = l + [niveau(leaf,pred,j,lvl+1)]
        return max(l)

for i in range(0,len(leaf)) :
    if leaf[i] == start :
        niv = niveau(leaf,pred,i,0)

startC = 0
for i in range(0,len(pred)) :
    if inte == pred[i] :
        startC = i
        break
print inte
print start
del(i)
del(j)
del(p)

def weight(pred,leaf,w,p,listW,lvl) :
    if leaf[p] == [] :
        return w[p]
    else :
        listW[lvl + 1]
        s = w[p]
        save = w[p]
        l = []
        for i in leaf[p] :
            for j in range(0,len(pred)) :
                if pred[j] == i :
                    a = weight(pred,leaf,w,j,listW,lvl + 1)
                    if type(a) == int :
                        l = l + [a]
                        s += a
                        listW[lvl + 1] = listW[lvl + 1] + [a]
                    else :
                        s += a[lvl + 1][-1]
                        l = l + [a[lvl + 1][-1]]
                        #for k in range(lvl + 2, niv + 1) :
                            #listW[k] = listW[k] + [a[k]]

        if min(l) != max(l) :
            print 'difference = ' + str(max(l) - min(l))
            print save 
            print l         
        listW[lvl] = listW[lvl] + [s]
        return listW
        
t = time.time()            
weight(pred,leaf,w,startC,[[]] * (niv + 1),0)
print time.time() - t

f.close()