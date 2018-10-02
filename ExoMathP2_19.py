# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:39:10 2013

@author: Nicolas
"""

from math import e

n=-1
while type(n)!=int or n<0:
    n=input('rang : ')

I=e-1

for i in range(1,n+1):
    I=e-i*I
    
print I