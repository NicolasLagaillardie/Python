# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:22:31 2013

@author: Nicolas
"""

# Le jeu de la vie

from Tkinter import *

class Can(Canvas):


    def __init__(self):
        
            #Variables
        
        self.vivants      = [] # Cases déjà remplies
        self.running    = 1  # Type de partie en cours
        self.couleur    = ["Bleus"]
        self.color      = ["#0000FF"]
        
            #Interface
        
        self.clair      = "light blue"
        self.fonce      = "navy blue"
        self.police1    = "Times 17 normal"
        self.police2    = "Arial 10 normal"
        self.police3    = "Times 15 bold"
        self.can        = Canvas.__init__(self, width =446, height = 430, bg=self.fonce, bd=0)
        
        self.grid(row=1, columnspan =5)

            # Joueur en cours
        
        self.joueur = 1
        self.create_rectangle(20,400,115,425,fill=self.clair)
        self.create_text(35, 405, text ="Joueur :", anchor = NW, fill = self.fonce, font= self.police2)
        self.indiccoul = self.create_oval(85, 405, 100, 420, fill = self.color[1])
        
            #Bouton Nouveau Jeu
        
        self.create_rectangle(330,400,420,425,fill=self.clair)
        self.create_text(340, 405, text ="Nouveau jeu", anchor = NW, fill = self.fonce, font= self.police2)
        
            #Création des cases
        
        self.ovals = []
        for y in range(10, 390, 55):
            for x in range(10, 437, 63):
                self.ovals.append(self.create_oval(x, y, x + 50, y + 50 , fill= "white"))
                
            #En cas de click
                
        self.bind("<Button-1>", self.click)
        
            # Pour relier à la fin les coordonnées des centres des cases
        
        self.coordscentres = []
        
            # Comptabilisation des suites de pièces
        
        self.rouges, self.jaunes = 0,0