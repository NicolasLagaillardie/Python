# -*- coding: cp1252 -*-
def bissextile(annee):
    if annee%4!=0:
        print annee,' n\'est pas une ann�e bissextile'
    else:
        if annee%100==0:
            if annee%400==0:
                print annee,' est bissextile'
            else:
                print annee,' n\'est pas une ann�e bissextile'
        else:
            print annee,' est une ann�e bissextile'
