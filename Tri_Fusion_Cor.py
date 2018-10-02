# -*- coding: cp1252 -*-

def Tri_Fusion(l):
    """ Tri Fusion - O(nlog(n)) """
    def Tri_Fusion_interne(l):
        if len(l)<2: return l
        return Merge( Tri_Fusion_interne(l[:len(l)//2]), Tri_Fusion_interne(l[len(l)//2:]))
    l[:] = Tri_Fusion_interne(l)