# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:51:01 2013

@author: Nicolas
"""

n=-1
while type(n)!=int or n<1 : #Conditions : n entier positif > 1
    n=input('Rentrer n : ')

somme=0.0  #Somme

for k in range (1,n+1): #Calcul de la somme
    somme=somme+float(1)/float(k)
    
print somme