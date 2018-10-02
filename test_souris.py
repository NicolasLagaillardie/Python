# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:53:55 2016

@author: Nicolas
"""

##
#  Move cursor to X,Y on screen
#
#   by ADcomp - www.ad-comp.be
##

X = 600
Y = 600

import gtk
import gobject

def run():
    display = gtk.gdk.display_get_default()
    screen = gtk.gdk.screen_get_default()
    display.warp_pointer(screen, X, Y)
    gtk.main_quit()

gobject.idle_add(run)
gtk.main()