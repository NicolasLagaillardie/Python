# -*- coding: cp1252 -*-

def Tri_Radix16(l):
    """ Tri Radix en passant en hexadécimaux - O(n) """
    for i in range(len(l)): l[i] = hex(l[i]).replace('L','')
    maxi=max(l)
    nbmaxi = len(maxi)-2
    ll = []
    for i in xrange(nbmaxi): ll.append([])
    for j in xrange(nbmaxi):
        for k in xrange(17):
            ll[j].append([])
    for i in l:
        ll[len(str(i))-3][16].append(i)  ## Plantage parfois encore non compris
##        except Exception, err: print err, i, nbmaxi, maxi
    for i in xrange(nbmaxi):
        for j in reversed(xrange(2,i+3)):
            for k in ll[i][16]:
                ll[i][int('0x'+str(k)[j],16)].append(k)
            ll[i][16]=[]
            for m in xrange(16): ll[i][16].extend(ll[i][m])
            for m in xrange(16): ll[i][m]=[]
    lll = []
    for i in xrange(nbmaxi): lll.extend(ll[i][16])
    for i in range(len(l)): l[i] = int(lll[i],16)