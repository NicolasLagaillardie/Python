# -*- coding: cp1252 -*-

def Merge(l1, l2):
    """ Tri 2 listes triées """
    l = []
    i = j =0
    n1=len(l1)
    n2=len(l2)
    while True:
        if i<n1 and j<n2:
            if l1[i]<l2[j]:
                l.append(l1[i])
                i+=1
            else:
                l.append(l2[j])
                j+=1
        elif i>=n1:
            l.extend(l2[j:])
            break
        else:
            l.extend(l1[i:])
            break
    return l