Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  Afficher la source en plein écran   copier dans le presse papier
#necessaire pour les threads
import threading

#classe qui défini notre thread
class MyThread (threading.Thread):
	#methode qui initialise la classe
	def __init__ (self,Fenetre):
		#Pour initialiser le thread en lui-meme
		#le parametre target(=run) indique la methode lancee
		#lors de la creation du thread
		threading.Thread.__init__ (self, target=self.run)
	#methode principale du thread
	def run (self):
		#ici le code de votre thread

#creation de notre thread
Thread1 = MyThread ()

#lancement du thread
#ne surtout pas modifier la methode start
#seule la methode run doit etre utilisee
Thread1.start()
