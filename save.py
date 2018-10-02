# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:33:40 2015

@author: Nicolas
"""

""""    
    
    #Inutile : fait tourner l'axe Z' vers X' et Y' pour paralleliser Z et Z'
    
    d2 = np.array(x)
    d1 = np.array([0,0,1])

    theta = np.sign(asin(np.vdot(d1,d2)/(np.linalg.norm(a,2)*np.linalg.norm(b,2))))*acos(np.vdot(d1,d2)/(np.linalg.norm(a,2)*np.linalg.norm(b,2)))
    
    rotaZtoX = np.array([[cos(theta),0,sin(theta)],[0,1,0],[-sin(theta),0,cos(theta)]])
    
    liste = []
    
    for i in coord :
        M = np.dot(rotaZtoX,np.array([[i[0]],[i[1]],i[2]]))
        liste.append([list(M[0]),list(M[1]),list(M[2])])
        
    coord = deepcopy(liste)
    
    a,b,c = 0,0,0
    while a == b or a == c or b == c :
        a,b,c = randint(0,len(coord)-1),randint(0,len(coord)-1),randint(0,len(coord)-1)
    
    A = np.array([[coord[a][0],coord[b][0],coord[c][0],1], [coord[a][1],coord[b][1],coord[c][1],1], [coord[a][2],coord[b][2],coord[c][2],1]])
    B = np.array([0,0,0])
    x = np.linalg.solve(A, B)
    
    d2 = np.array(x)
    d1 = np.array([0,0,1])

    theta = np.sign(asin(np.vdot(d1,d2)/(np.linalg.norm(a,2)*np.linalg.norm(b,2))))*acos(np.vdot(d1,d2)/(np.linalg.norm(a,2)*np.linalg.norm(b,2)))
    
    rotaZtoX = np.array([[cos(theta),0,sin(theta)],[0,1,0],[-sin(theta),0,cos(theta)]])
    
    liste = []
    
    for i in coord :
        M = np.dot(rotaZtoX,np.array([[i[0]],[i[1]],i[2]]))
        liste.append([list(M[0]),list(M[1]),list(M[2])])
        
    pts = deepcopy(liste)   
    
    """
    
    #Points les plus éloignés
    
    liste = []
    
    """
    maxi = 0
    pt1 = 0
    pt2 = 0
        
    for i in range(len(pts)):
        for j in range(len(pts)):
            d = distance(pts[i],pts[j])
            if d>maxi :
                maxi = d
                pt1 = i
                pt2 = j
                
    liste.append(pts[pt1])
    liste.append(pts[pt2])
    
    """