# -*- coding: utf-8 -*-
"""
Created on Thu Dec 05 09:28:18 2013

@author: Nicolas
"""

def p1(x,n):
    s=1.0
    for i in range(0,n+1):
        s=s+i*(x**i)
    return s
    
def p2(x,n):
    s=0.0
    for i in range(0,n):
        s=(s+(n-i))*x
    return s+1
    
from scipy import *
val=linspace(0.8,1,100)
res=[p1(x,100)-p2(x,100) for x in val]
print val
print res