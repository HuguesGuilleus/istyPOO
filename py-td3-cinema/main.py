#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import obj
import gui.edit
import gui.index
import gui.menu
import gui.new


builder = Gtk.Builder()
builder.add_from_file("win.glade")

# Valeur pour le développement
f = obj.FunctionaryDB.new()
f.setId("Peter Wiggins")
f["mail"] = "peter.wiggins@fai.mil"
f.save()
f = obj.FunctionaryDB.new()
f.setId("Valentine Wiggins")
f["mail"] = "valentine.wiggins@fai.mil"
f.save()


print(f"On passe à la suite")

l = obj.LocationDB.new()
l.setId("America")
l.save()



win = builder.get_object("win")
win.show_all()
win.connect("destroy", Gtk.main_quit)

builder.get_object("rm").connect("clicked", gui.menu.show)
builder.get_object("save").connect("clicked", gui.menu.show)
gui.menu.init(builder, [
	obj.GuestDB,
	obj.FunctionaryDB,
	obj.ScreeningDB,
	obj.LocationDB,
])

win.maximize()
Gtk.main()
