# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:19:01 2013

@author: Nicolas
"""

from math import log

n=-1
while type(n)!=int or n<=0: # Conditions : n n entier strictement poitif
    n=input('n ? ')

s=0
for i in range(1,n+1):	# Calcul de la suite Un
    s=s+(float(1)/float(i))
    
s=float(s)/(float(log(n)))  # Division par ln(n)

print s