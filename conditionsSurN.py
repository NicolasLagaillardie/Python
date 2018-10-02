# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:48:29 2013

@author: Nicolas
"""

n=-1
while type(n)!=int or n<0 or n==1 or n%13==0:   #Conditions invoquées
    n=input('n ? : ')