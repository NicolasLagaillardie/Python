# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 18:18:27 2015

@author: lafam
"""

import numpy as np
import matplotlib.pyplot as plt
from random import *
from mpl_toolkits.mplot3d import Axes3D

def f(x,y) :
    np.log(abs(np.sin(x**10) + np.cos(y**10)) + 1.0)


ax = Axes3D(plt.figure())
X = np.arange(-1, 1, 0.02)
Y = np.arange(-1, 1, 0.02)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
ax.plot_surface(X, Y, Z)

plt.show()