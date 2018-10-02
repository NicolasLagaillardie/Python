# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 13:47:31 2015

@author: lafam
"""

import numpy as np
import matplotlib.pyplot as plt
from random import *



def f(x):
    return np.sin(x)*np.exp(x/20)


def GradSearch_A_Minimum(f,a,b,eps,n):
    def Df(z,h):
        return (f(z + h) - f(z))/h
    x0 = uniform(a,b)
    xMin = x0
    for k in range(0,n):
        plt.plot(x0, f(x0),"ro")
        if f(x0) < f(xMin) :
                xMin = x0
        if Df(x0 - eps*Df(x0,eps)/abs(Df(x0,eps)), eps)*Df(x0, eps) <= 0 :
            bol = randint(0,2)
            if bol == 0 :
                x0 = uniform(a, x0)
            else:
                x0 = uniform(x0, b)
        else:
            x0 = x0 - eps*Df(x0,eps)/abs(Df(x0,eps))
    return xMin





def Affiche_GradSearch_A_Minimum(f,a,b,eps,n):
    X=linspace(a,b,1000)
    Y=f(X)
    plt.plot(X,Y,"b")
    def Df(z,h):
        return (f(z + h) - f(z))/h
    x0 = uniform(a,b)
    xMin = x0
    for k in range(0,n):
        plt.plot(x0, f(x0),"ro")
        if f(x0) < f(xMin) :
                xMin = x0
        if Df(x0 - eps*Df(x0,eps)/abs(Df(x0,eps)), eps)*Df(x0, eps) <= 0 :
            bol = randint(0,2)
            if bol == 0 :
                x0 = uniform(a, x0)
            else:
                x0 = uniform(x0, b)
        else:
            x0 = x0 - eps*Df(x0,eps)/abs(Df(x0,eps))
    plt.title("Une recherche de minimum pour f(x)=sin(x)*exp(x/20), eps=0,1, n=500")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()
    return xMin




def GradSearchMin(f,a,b,eps,N,n):
    xMin = a
    for k in range(0,N):
        x0 = GradSearch_A_Minimum(f,a,b,eps,n)
        if f(x0) < f(xMin) :
            xMin = x0
    return xMin

print GradSearchMin(f,0,50,0.1,10,500)

        
    