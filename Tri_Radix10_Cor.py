# -*- coding: cp1252 -*-

def Tri_Radix10(l):
    """ Tri Radix - O(n) """    
    maxi=max(l)
    ll = []
    for i in xrange(len(str(maxi))):
        ll.append([])
    for j in xrange(len(str(maxi))):
        for k in xrange(11):
            ll[j].append([])
    for i in l:
        ll[len(str(i))-1][10].append(i)
    for i in xrange(len(str(maxi))):
        for j in reversed(xrange(i+1)):
            for k in ll[i][10]:
                ll[i][int(str(k)[j])].append(k)
            ll[i][10]=[]
            for m in xrange(10): ll[i][10].extend(ll[i][m])
            for m in xrange(10): ll[i][m]=[]
    lll = []
    for i in xrange(len(str(maxi))):
        lll.extend(ll[i][10])
    l[:] = lll[:]