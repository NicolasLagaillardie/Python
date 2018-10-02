# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 14:06:22 2017

@author: Lagai
"""

f = open("day9.txt","r")
doc = f.read()
doc = doc[:-1]

compt = 0
ignored = 1
k = 0
i = 0

charac = 0

while i < len(doc):
    if doc[i] == '!' :
        i += 2
    elif doc[i] == '{' :
        compt += 1
        k += compt
        i += 1
    elif doc[i] == '}' :
        compt -= 1
        i += 1
    elif doc[i] == '<' :
        ignored = 1
        i += 1
        while ignored == 1:
            if doc[i] == '!' :
                i += 2
            else :
                if doc[i] == '>' :
                    ignored = 0
                else :
                    charac += 1
                    i += 1
    else :
        i += 1

print charac 
print k

f.close()