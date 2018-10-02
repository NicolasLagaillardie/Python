# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import numpy as np

def makemat(k) :
    mat = [[1]]
    rowM = 1
    rowC = 0
    sensC = 0
    sensR = 0
    colM = 1
    colC = 1
    
    i = 2
    
    while i < k :
        if (colC <= colM) and (sensC == 0) :
            mat[rowC] = mat[rowC] + [i]
            colC += 1
            i += 1
        elif (colC > 1) and (sensC == 1) :
            mat[rowC] = [i] + mat[rowC]
            colC -= 1
            i += 1
        else :
            if (rowC > 0) and (sensR == 0) :
                mat[rowC-1] = mat[rowC-1] + [i]
                rowC -= 1
                i += 1
            elif (rowC == 0) and (sensR == 0) :
                mat = [[i]] + mat
                i += 1
                sensR = abs(sensR-1)
                rowM += 1
                sensC = abs(sensC-1)
                colM += 2
            elif (rowC < rowM) and (sensR == 1) :
                mat[rowC] = [i] + mat[rowC]
                rowC += 1
                i += 1
            else :
                mat = mat + [[i]]
                i += 1
                sensR = abs(sensR-1)
                rowM += 1
                sensC = abs(sensC-1)
        
    return mat

def aux(nbr,pred,mat,row,column):

    t = time.time()
	
    try :
        if mat[row][column+1] - mat[row][column] < 2 :
            if mat[row][column+1] not in nbr :
                nbr = nbr + [mat[row][column+1]]
            pred[mat[row][column+1]] = min(pred[mat[row][column]] + 1,pred[mat[row][column+1]])
    except :
        0
    try :
        if mat[row+1][column] - mat[row][column] < 2 :
            if mat[row+1][column] not in nbr :
                nbr = nbr + [mat[row+1][column]]
            pred[mat[row+1][column]] = min(pred[mat[row][column]] + 1,pred[mat[row+1][column]])
    except :
        0
    try :
        if mat[row-1][column] - mat[row][column] < 2 :
            if mat[row-1][column] not in nbr :
                nbr = nbr + [mat[row-1][column]]
            pred[mat[row-1][column]] = min(pred[mat[row][column]] + 1,pred[mat[row-1][column]])
    except :
        0
    try :
        if mat[row][column-1] - mat[row][column] < 2 :
            if mat[row][column-1] not in nbr :
                nbr = nbr + [mat[row][column-1]]
            pred[mat[row][column-1]] = min(pred[mat[row][column]] + 1,pred[mat[row][column-1]])
    except :
        0
        
    return nbr,pred,(time.time()-t)

def RC(k,mat) :

    t = time.time()
    
    c = 1
    
    while c**2 < k :
        c += 2
    
    row = 0
    column = 0
    
    for i in range(max(527/2-c/2-1,0),len(mat)) :
        if k in mat[i] :
            row = i
            for j in range(max(527/2-c/2-1,0),len(mat[i])) :
                if mat[i][j] == k :
                    column = j
                    return row,column,(time.time()-t)

def distance(nbr,pred,mat,row,column) :
    
    p = 0
	
    otA = 0
    otRC = 0
    
    t = time.time()
    
    while 1 not in nbr:
        [nbr,pred,tA] = aux(nbr,pred,mat,row,column)
        [row,column,tRC] = RC(nbr[p],mat)
		
        otA = max(otA,tA)
        otRC = max(otRC,tA)
		
        p += 1
        
    return len(nbr),pred[1],otA,otRC,(time.time()-t)


mat = makemat(527**2)

k = 5
nbr = [k]
pred = [k**2] * (k+2)
pred[k] = 0
row = 0
column = 0      
    
[row,column,t] = RC(nbr[0],mat)

print distance(nbr,pred,mat,row,column)

def addA(row,col,mat) :
    s = 0
    try :
        s += mat[row+1,col]
    except :
        0
    try :
        s += mat[row-1,col]
    except :
        0
    try :
        s += mat[row,col+1]
    except :
        0
    try :
        s += mat[row,col-1]
    except :
        0
    try :
        s += mat[row+1,col+1]
    except :
        0
    try :
        s += mat[row+1,col-1]
    except :
        0
    try :
        s += mat[row-1,col+1]
    except :
        0
    try :
        s += mat[row-1,col-1]
    except :
        0
        
        
    return s

def makemat2(k) :
    R = 1
    U = 1
    L = 2
    D = 2
    nbr = [1]

    s = 1001
    
    mat = np.zeros((s,s))
    row = s/2
    col = s/2
    mat[row,col] = 1
    
    while max(nbr) < k :
        for j in range(0,R) :
            mat[row,col+j+1] = addA(row,col+j+1,mat)
            nbr = [addA(row,col+j+1,mat)] + nbr
        col += R
        for j in range(0,U) :
            mat[row-j-1,col] = addA(row-j-1,col,mat)
            nbr = [addA(row-j-1,col,mat)] + nbr
        row -= U
        for j in range(0,L) :
            mat[row,col-j-1] = addA(row,col-j-1,mat)
            nbr = [addA(row,col-j-1,mat)] + nbr
        col -= L
        for j in range(0,D) :
            mat[row+j+1,col] = addA(row+j+1,col,mat)
            nbr = [addA(row+j+1,col,mat)] + nbr
        row += D
        
        R += 2
        U += 2
        L += 2
        D += 2
    
    for i in range(len(nbr)-1,-1,-1) :
        if nbr[i] > k :
            return nbr[i]