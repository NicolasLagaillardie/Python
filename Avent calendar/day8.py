# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 14:19:36 2017

@author: Lagai
"""

f = open("day81.txt","r")

docint = f.readlines()
doc = []

for i in docint :
    doc = doc + [i[:-1].split()]

var = []
w = []

def posi(vari,var):
    for i in range(0,len(var)) :
        if var[i] == vari :
            return i
            
def augm(line) :
    if line[1] == 'inc' :
        w[posi(i[0],var)] += int(i[2])
    else :
        w[posi(i[0],var)] -= int(i[2])
        
maxi = 0        

for i in doc :
    if i[0] not in var :
        var = var + [i[0]]
        w = w + [0]
    if i[4] not in var :
        var = var + [i[4]]
        w = w + [0]
        
    if i[5] == '>' :
        if w[posi(i[4],var)] > int(i[6]) :
            augm(i)
    if i[5] == '<' :
        if w[posi(i[4],var)] < int(i[6]) :
            augm(i)
    if i[5] == '==' :
        if w[posi(i[4],var)] == int(i[6]) :
            augm(i)
    if i[5] == '<=' :
        if w[posi(i[4],var)] <= int(i[6]) :
            augm(i)
    if i[5] == '>=' :
        if w[posi(i[4],var)] >= int(i[6]) :
            augm(i)
    if i[5] == '!=' :
        if w[posi(i[4],var)] != int(i[6]) :
            augm(i)
            
    maxi = max(maxi,max(w))
        

print 'doc =',
print doc
print 'les variables : var = ',
print var
print 'les poids : w =',
print w
 
print maxi