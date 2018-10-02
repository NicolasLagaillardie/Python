# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:21:02 2017

@author: Lagai
"""

from copy import deepcopy

f = open('day11.txt','r')
strC = f.readline()[:-1].split(',')

#strC = ['ne','ne','s','s']

def f(strC) :
    strN = []
    
    while strC != strN :
        strN = deepcopy(strC)
        inte = []
        for i in strC :
            #Pour ne
            if i == 'ne' :
                if 'sw' in inte :
                    inte.remove('sw')
                elif 'nw' in inte :
                    inte.remove('nw')
                    inte = inte + ['n']
                elif 's' in inte :
                    inte.remove('s')
                    inte = inte + ['se']
                else :
                    inte = inte + ['ne']
            #Pour se
            elif i == 'se' :
                if 'nw' in inte :
                    inte.remove('nw')
                elif 'sw' in inte :
                    inte.remove('sw')
                    inte = inte + ['s']
                elif 'n' in inte :
                    inte.remove('n')
                    inte = inte + ['ne']
                else :
                    inte = inte + ['se']
            #Pour nw
            elif i == 'nw' :
                if 'se' in inte :
                    inte.remove('se')
                elif 'ne' in inte :
                    inte.remove('ne')
                    inte = inte + ['n']
                elif 's' in inte :
                    inte.remove('s')
                    inte = inte + ['sw']
                else :
                    inte = inte + ['nw']
            #Pour sw
            elif i == 'sw' :
                if 'ne' in inte :
                    inte.remove('ne')
                elif 'se' in inte :
                    inte.remove('se')
                    inte = inte + ['s']
                elif 'n' in inte :
                    inte.remove('n')
                    inte = inte + ['nw']
                else :
                    inte = inte + ['sw']
            #Pour n
            elif i == 'n' :
                if 's' in inte :
                    inte.remove('s')
                elif 'se' in inte :
                    inte.remove('se')
                    inte = inte + ['ne']
                elif 'sw' in inte :
                    inte.remove('sw')
                    inte = inte + ['nw']
                else :
                    inte = inte + ['n']
            #Pour s
            else :
                if 'n' in inte :
                    inte.remove('n')
                elif 'nw' in inte :
                    inte.remove('nw')
                    inte = inte + ['sw']
                elif 'ne' in inte :
                    inte.remove('ne')
                    inte = inte + ['se']
                else :
                    inte = inte + ['s']
        strC = inte
        
    return len(strC)

maxi = 0
for i in range(1,len(strC)) :
    maxi = max(maxi,f(strC[:i]))
    
print maxi