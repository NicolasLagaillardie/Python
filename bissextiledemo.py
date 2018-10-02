# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:04:34 2013

@author: Nicolas
"""

global a
a=5

def essais(n):
    global a
    a=n
    
def bissextile(annee):
    if a>0:
        essais(a-1)
        if annee%400==0 or (annee%4==0 and annee%100!=0):
            print annee,' est bissextile'
        else:
            print annee,' n\'est pas une annee bissextile'
        print 'Il vous reste ',a,' essais'
    else:
        print 'Votre version de demonstration est terminee, veuillez visiter www.jecroisauperenoel.com'
        print 'pour plus d\'informations'