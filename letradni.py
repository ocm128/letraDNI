#!/usr/bin/env python
# -*- coding: latin-1 -*-

# First run tutorial.glade through gtk-builder-convert with this command:
# gtk-builder-convert letradni.glade letradni.xml

# coded by ocm128
# email: tdoc@tutamail.com


import pygtk
pygtk.require("2.0")
import gtk
import os
import sys


class LetraDni(object):
    
    def on_mainWindow_destroy(self, widget, data=None):
        gtk.main_quit()
    
    
    def on_entry1_activate(self, widget, data=None):
        
        try:
            self.labelTexto.set_text(self.calcula())
        except TypeError:
            pass
        
    def on_about_menu_item(self, widget, data=None):
        
        authors = [
        "ocm128 <tdoc@tutamail.com>"
        ]
        
        aboutDlg = gtk.AboutDialog()
        aboutDlg.set_transient_for(self.window) # sale encima de la principal
        aboutDlg.set_name("LetraDNI")
        aboutDlg.set_version("1.0")
        aboutDlg.set_authors(authors)
        aboutDlg.set_logo_icon_name     (gtk.STOCK_EDIT)
        aboutDlg.show()
        
        aboutDlg.connect("response", lambda d,response: d.destroy())
    
        

    def calcula(self):
        cad = "trwagmyfpdxbnjzsqvhlcket"
        num = self.entry1.get_text()
        try:
            aux = int(num)
            aux = aux % 23
            aux + 1
            return num + cad[aux].upper()
        except ValueError:
            self.labelTexto.set_text("Solo digitos")
        finally:
            self.entry1.set_text("")
            


    def __init__(self):
        
        builder = gtk.Builder()
        builder.add_from_file("letradni.xml")
        #builder.connect_signals({ "on_mainWindow_destroy" : gtk.main_quit })
        self.window = builder.get_object("mainWindow")
        self.labelTexto = builder.get_object("labelTexto")
        self.entry1 = builder.get_object("entry1")
        self.button1 = builder.get_object("")
        builder.connect_signals(self)
        

    def main(self):
        self.window.show()
        gtk.main()

if __name__ == "__main__":
    app = LetraDni()
    app.main()

