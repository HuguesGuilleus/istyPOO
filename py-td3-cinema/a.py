#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from storage.struct import Struct as Struct
from storage.db import DB as DB

class Salle(Struct):
	"""Une salle (pour la diffusion de cinéma, concert...)."""
	def __init__(self, db):
		super(Salle, self).__init__({
			"*addresse": "",
			"nbPlace": 0,
			"type": "cinema",
		}, db)

d = DB("data/t.db", Salle)

Salle(d).fromJSON('{"nbPlace": 400, "type": "cinema", "addresse": "4856 rue yolo"}').save()
Salle(d).fromJSON('''{"nbPlace": 90000,"type": "petite boite de nuit", "addresse": "36 avenue ma bite"}''').save()


for i, v in d.items():
	print(f"i: {type(i)} :: {i}")
	print(f"v: {type(v)} :: {v}")
	print()
