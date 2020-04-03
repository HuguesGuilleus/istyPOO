#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from . import index

builder = None

def init(b, dbs):
	global builder
	builder = b

	parent = builder.get_object("menuZone")
	for d in dbs:
		b = Gtk.Button.new_with_label(d.name())
		b.connect("clicked", click(d))
		b.show()
		parent.add(b)

	builder.get_object("menu").connect("clicked", show)
	show(None)

def click(d):
	return lambda _: index.index(builder, d)

def show(_):
	builder.get_object("menuZone").show()
	builder.get_object("editZone").hide()
	builder.get_object("indexList").hide()
	builder.get_object("newZone").hide()
	builder.get_object("save").hide()
	builder.get_object("rm").hide()
	builder.get_object("new").hide()
