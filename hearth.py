# -*- coding: utf-8 -*-
"""
Created on Thu Dec 05 09:33:35 2013

@author: Nicolas
"""


import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,100)
plt.plot(x,np.sin(x))  # on utilise la fonction sinus de Numpy
plt.ylabel('fonction sinus')
plt.xlabel("l'axe des abcisses")
plt.show()