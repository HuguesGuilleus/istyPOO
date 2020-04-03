#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from . import edit

db = None
builder = None
initialize = False

def init(b, d):
	"Prépare la création d'un nouvel objet."
	global db, builder, initialize
	builder = b
	db = d

	builder.get_object("indexList").hide()
	builder.get_object("newZone").show()
	builder.get_object("newName").set_text("")

	if not initialize:
		initialize = True
		builder.get_object("newNext").connect("clicked", next)

def next(_):
	"Créé le nouvel objet"
	s = db.new()
	s.setId(builder.get_object("newName").get_text())
	s.save()
	edit.create(builder, s)
