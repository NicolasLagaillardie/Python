# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 16:58:01 2017

@author: Lagai
"""

from copy import deepcopy
import numpy as np

l = np.array([14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4])
#l = np.array([0,2,7,0])
            
a = [l.tolist(),0]

while a[0] not in a[1:] :
    p = l.argmax()
    c = deepcopy(l[p])
    l[p] = 0
    l = l + c/l.size
    m = min(l.size,p+1+c%l.size)
    l[p+1:m] = l[p+1:m] + 1
    l[:max((c%l.size)-(m-p)+1,0)] = l[:max((c%l.size)-(m-p)+1,0)] + 1
    a = [l.tolist()] + a
    
print len(a) - 2
for i in range(1,len(a)) :
    if a[i] == a[0]:
        print i
        break