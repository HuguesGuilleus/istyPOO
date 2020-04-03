#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk

allValues = {}
struct = None
removeID = 0

def create(builder, s):
	"""Edite une Struct dans l'interface utilisateur."""
	global allValues, struct, removeID
	allValues = {}
	struct = s

	builder.get_object("indexList").hide()
	builder.get_object("newZone").hide()
	builder.get_object("save").show()
	builder.get_object("rm").show()
	builder.get_object("new").hide()

	rm = builder.get_object("rm")
	rm.show()
	if removeID: rm.disconnect(removeID)
	removeID = rm.connect("clicked", lambda _ : s.autoremove())

	builder.get_object("editZone").show()
	builder.get_object("editHead").set_text(f"{s.__class__.__name__}: {s.idValue}")

	editTable = builder.get_object("editTable")
	editTable.foreach(lambda e : editTable.remove(e))
	i = 0
	for k, v in s:
		i += 1
		editTable.insert_row(i)
		label = Gtk.Label(k)
		editTable.attach(label, 0, i, 1, 1)
		button = None
		if type(v) == type(""):
			button = Gtk.Entry()
			button.set_text(v)
			button.connect("changed", changeStr(k, button))
		elif type(v) == type(False):
			button = Gtk.Switch()
			button.set_active(v)
			button.connect("state-set", changeBool(k, button))
		elif type(v) == type(0):
			button = Gtk.SpinButton()
			button.set_adjustment(Gtk.Adjustment(v, 0, 10000, 1, 10, 0))
			button.connect("value-changed", changeNb(k, button))
		else:
			button = listStore(k, s.getDB(k))
			if button == None: continue
		editTable.attach(button, 1, i, 1, 1)
	editTable.show_all()

def save(_):
	if not struct: return
	for k, v in allValues.items():
		struct[k] = v
	print(f"struct: {type(struct)} :: {struct}")

def changeStr(k, b):
	"""Renvoie une fonction pour enregistrer dans le tempons la valeur de
	l'entré textuelle"""
	return lambda _ : allValues.__setitem__(k, b.get_text())

def changeBool(k, b):
	"Renvoie une fonction pour enregistrer dans le tempons la valeur du switch"
	return lambda _, v : allValues.__setitem__(k, v)

def changeNb(k, b):
	return lambda _ : allValues.__setitem__(k, int(b.get_value()))

def listStore(key, db):
	if db == None: return None

	l = Gtk.ListStore(str, str)
	for k, v in db.items():
		l.append([str(k), v.idValue])

	combo = Gtk.ComboBox.new_with_model_and_entry(l)
	combo.connect("changed", lambda _ : changeListStore(key, combo))
	combo.set_entry_text_column(1)
	return combo

def changeListStore(key, combo):
	i = combo.get_active_iter()
	if i == None: return
	v = combo.get_model()[i][0]
	allValues.__setitem__(key, bytes(v, "utf-8"))
