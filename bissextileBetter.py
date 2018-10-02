# -*- coding: cp1252 -*-
def bissextile(annee):
    if (annee%4==0 and annee%100!=0) or annee%400==0:
		print annee,' n\'est pas une année bissextile'
	else:
		print annee,' est une année bissextile'
