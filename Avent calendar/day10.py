# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:16:32 2017

@author: Lagai
"""

from copy import deepcopy

l = [i for i in range(0,256)]
#l = [0,1,2,3,4]

position = 0

skipSize = 0

seq = [206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3]

"""
for i in seq :
    inte = deepcopy(l[position:min(len(l),i+position)] + l[0:max(0,(i+position)-len(l))])
    inte.reverse()
    l[position:min(len(l),i+position)] = inte[:len(l[position:min(len(l),i+position)])]
    l[0:max(0,(i+position)-len(l))] = inte[len(l[position:min(len(l),i+position)]):]  

    position = (i + skipSize + position)%len(l)
    skipSize += 1
    
print l[0]*l[1]
"""

ASCII = []
seqStr = '206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3'

for i in seqStr :
    ASCII = ASCII +[ord(str(i))]

ASCII = ASCII + [17, 31, 73, 47, 23]

for j in range(0,64) :
    for i in ASCII :
        inte = deepcopy(l[position:min(len(l),i+position)] + l[0:max(0,(i+position)-len(l))])
        inte.reverse()
        l[position:min(len(l),i+position)] = inte[:len(l[position:min(len(l),i+position)])]
        l[0:max(0,(i+position)-len(l))] = inte[len(l[position:min(len(l),i+position)]):]  
    
        position = (i + skipSize + position)%len(l)
        skipSize += 1

XOR =''
for i in range(0,len(l),16) :
    s = l[i]
    for j in range(i+1,i+16) :
        s = s ^ l[j]
    XOR = XOR + format(s, '02x')
    
print XOR