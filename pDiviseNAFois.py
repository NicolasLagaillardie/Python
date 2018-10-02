# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:58:35 2013

@author: Nicolas
"""

n='a'
while type(n)!=int or n==0: # n entier non nul
    n=input('n ? ')
p='a'
while type(p)!=int or p==0: # p entier non nul
    p=input('p ? ')

a=0
for i in range(1,n+1):  # Boucler les multiples de p divisant n
    if n%(i*p)==0:
        a+=1

print a