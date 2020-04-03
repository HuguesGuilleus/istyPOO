#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from . import edit
from . import new

newID = 0

def index(builder, db):
	global newID

	builder.get_object("editZone").hide()
	builder.get_object("menuZone").hide()
	builder.get_object("newZone").hide()
	builder.get_object("save").hide()
	builder.get_object("rm").hide()
	builder.get_object("new").show()
	if newID: newID = builder.disconnect(newID)
	newID = builder.get_object("new").connect("clicked", lambda _: new.init(builder, db))

	parent = builder.get_object("indexList")
	parent.show()
	parent.foreach(lambda e : parent.remove(e))
	for k, v in db.items():
		b = Gtk.Button.new_with_label(v.idValue)
		b.connect("clicked", click(builder, v))
		b.show()
		parent.add(b)

def click(builder, v):
	return lambda _: edit.create(builder, v)
