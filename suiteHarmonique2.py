# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:49:09 2013

@author: Nicolas
"""

n=-1
while type(n)!=int or n<0 : # Conditions sur n
    n=input('Rentrer n : ')

somme=0.0  # Somme

for k in range (1,n+1): # Calcul de la somme
    somme=somme+float((-1)**k)/float(2*k+1)
    
print somme