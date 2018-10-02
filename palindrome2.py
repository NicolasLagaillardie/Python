# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
C:\Users\Nicolas\.spyder2\.temp.py
"""
def palindrome(ch):
    ch=list(str(ch))
    l=ch[len(ch)/2+len(ch)%2:len(ch)]
    l.reverse()
    if ch[0:len(ch)/2]==l:
        return True
    else:
        return False