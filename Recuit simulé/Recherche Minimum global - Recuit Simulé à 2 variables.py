# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 17:14:19 2015

@author: lafam
"""

import numpy as np
import matplotlib.pyplot as plt
from random import *
import math
from mpl_toolkits.mplot3d import Axes3D






def f(x,y) :
    return np.exp(y/8.0)*np.cos(x) - np.exp(x/8.0)*np.sin(y)

def inInterv(a,b,x):
    return a<=x and x<=b

def hexString(n) :
    """renvoie une chaine de caractere de type hexstring (pour n=6) representant une couleur"""
    S="#"
    for i in range (0,n):
        S=S+str(randint(0,9))
    return S  



def GradSearch_A_Minimum(f,a,b,c,d,eps,n):
    def Dfx(x,y,h):
        return (f(x + h, y) - f(x, y))/h
    def Dfy(x,y,h):
        return (f(x, y + h) - f(x, y))/h
    x0, y0 = uniform(a,b), uniform(c,d)
    xMin, yMin = x0, y0
    for k in range(0,n):
        if f(x0,y0) < f(xMin, yMin) :
                xMin, yMin = x0, y0
        if Dfx(x0 - eps*Dfx(x0, y0, eps)/abs(Dfx(x0, y0, eps)), y0, eps)*Dfx(x0, y0, eps) <= 0 and Dfy(x0, y0 - eps*Dfy(x0, y0, eps)/abs(Dfy(x0, y0, eps)), eps)*Dfy(x0, y0, eps) <= 0:
            bol = randint(0,4)
            if bol == 0 :
                x0, y0 = uniform(x0, b), uniform(y0, d)
            elif bol == 1 :
                x0, y0 = uniform(a, x0), uniform(y0, d)
            elif bol == 2 :
                x0, y0 = uniform(a, x0), uniform(c, y0)
            else :
                x0, y0 = uniform(x0, b), uniform(c, y0)
        else:
            x0, y0 = x0 - eps*Dfx(x0, y0, eps)/abs(Dfx(x0, y0, eps)) , y0 - eps*Dfy(x0, y0, eps)/abs(Dfy(x0, y0, eps))
    return xMin, yMin



def GradSearch_A_MinimumPlot(f,a,b,c,d,eps,n):
    ax = Axes3D(plt.figure())    
    X = np.arange(a, b, 0.4)
    Y = np.arange(c, d, 0.4)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    ax.plot_wireframe(X, Y, Z)
    def Dfx(x,y,h):
        return (f(x + h, y) - f(x, y))/h
    def Dfy(x,y,h):
        return (f(x, y + h) - f(x, y))/h
    x0, y0 = uniform(a,b), uniform(c,d)
    xMin, yMin = x0, y0
    strcolor = hexString(6)
    for k in range(0,n):
        ax.scatter(x0, y0, f(x0, y0), c = strcolor)
        if f(x0,y0) < f(xMin, yMin) :
                xMin, yMin = x0, y0
        if (Dfx(x0 - eps*Dfx(x0, y0, eps)/abs(Dfx(x0, y0, eps)), y0, eps)*Dfx(x0, y0, eps) <= 0 and Dfy(x0, y0 - eps*Dfy(x0, y0, eps)/abs(Dfy(x0, y0, eps)), eps)*Dfy(x0, y0, eps) <= 0) or not(inInterv(x0,a,b)) or not(inInterv(y0,c,d)) :
            strcolor = hexString(6)            
            bol = randint(0,4)
            if bol == 0 :
                x0, y0 = uniform(x0, b), uniform(y0, d)
            elif bol == 1 :
                x0, y0 = uniform(a, x0), uniform(y0, d)
            elif bol == 2 :
                x0, y0 = uniform(a, x0), uniform(c, y0)
            else :
                x0, y0 = uniform(x0, b), uniform(c, y0)
        else:
            x0, y0 = x0 - eps*Dfx(x0, y0, eps)/abs(Dfx(x0, y0, eps)) , y0 - eps*Dfy(x0, y0, eps)/abs(Dfy(x0, y0, eps))
    ax.scatter(xMin, yMin, f(xMin, yMin), c = "green", s=45**2)
    plt.title("Une recherche de minmum de f(x,y) = exp(y/8.0)*cos(x) - exp(x/8.0)*sin(y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    return xMin, yMin
    


print GradSearch_A_MinimumPlot(f,-5,5,-5,5,0.01,3000)

