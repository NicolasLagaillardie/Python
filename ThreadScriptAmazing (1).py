Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #-*- coding:Utf-8 -*-
import random
from Queue import *
from threading import Thread
import time
 
enStock = Queue(10)#notre pile, qui peut contenir 10 éléments max( 0 pour enlever la limite)
 
class Magasin(Thread):
    """ Le 'producteur' : va remplir ses rayons de paquets de schtroumpfs """
    def __init__(self):
        self.ouvert = True
        Thread.__init__(self)
 
    def run(self):
        while self.ouvert :
 
            while not enStock.full() :
                try :
 
                    enStock.put("ajout d'un paquet de schtroumpf",True,1000)
                    ### le Magasin va ajouter un paquet dans le rayon, et s'il y a plus de place,
                    ### va attendre pendant 1 seconde qu'un paquet soit acheté .
                except Full,e :
                    print(" Il n'y a pas de place pour un paquet ! ");
 
                else:
                    print(" On ajoute un paquet de schtroumpfs dans le rayon")
 
            time.sleep(10)
            #on attend 10 secondes avant que le magasin aille alimenter le rayon
 
class Client(Thread):
    """ le consommateur, va prendre un/des paquet(s) de schtroumpf """
    def __init__(self,faim,numero):
        self.jAiFaim = faim
        self.numero = numero
        Thread.__init__(self)
    def run(self):
        while self.jAiFaim :
            time.sleep(1)
            #le client arrive au bout d'une seconde au rayon
 
            ok=False
            paquet = random.randint(1,4)
            #nombre de paquet qu'il va prendre
            i=1
            print(" Le client n° "+str(self.numero)+" veut "+str(paquet)+" paquet(s) de schtroumpfs")
            while i<=paquet :
                try:
                    enStock.get(True,500)
                    ok = True
                    print(" n° "+ str(self.numero) + " : Prend un paquet")
 
                except Empty, e:
                    ok = False
                    break
                else:
                    i+=1
            if ok :
                print(" Il reste " + str( enStock.qsize() ) +" paquet(s) de schtroumpfs")
            else :
                print(" n° "+ str(self.numero) + " : Il n'y a pas assez de paquets")
            self.jAiFaim = False
 
if __name__=='__main__':
    magasin = Magasin()
    magasin.ouvert = True
    print("##### Le magasin ouvre ses portes #####")
    magasin.start()
 
    i=1
    while i < 10:
        Client(faim = True ,numero = i).start()
        i=i+1
 
    time.sleep(60)
    magasin.ouvert=False
    print("##### Le magasin ferme ses portes #####")
